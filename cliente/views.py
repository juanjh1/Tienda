from django.shortcuts import render, redirect
from  django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from products.models import Product
from coments.models import Comment
from django.db.models import Count
from django.contrib import messages
# Create your views here.

def index (request):
    
    mas_comentado = Comment.objects.values('product').annotate(num_veces=Count('product')).order_by('-num_veces')
    
    products= []
    for grup in mas_comentado:
        if len(products) < 3:
            products.append( Product.objects.filter(id=grup['product']).first())
    
    context = {

        'products': products
    }
    
    
    return render (request, 'index.html', context)


def register(request):

    # verifica si un usuario esta logeado, y dependiendo lo redirige a una ruta dirente 
    if request.user.is_authenticated:

        return redirect('/productos/')
    else:
        return render(request, 'logs/register.html ')

    
def Create_user(request):
    name = request.POST['name']
    lastname = request.POST['lastname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    if len(password) <= 10 and len(password) >= 6: # valida los campos 
        valid_username = User.objects.filter(username=username).first()
        valid_email = User.objects.filter(email=email).first()

        if valid_email is None and valid_username is None:# valida que ingrese los campos correctamente 
            password_enc = make_password(password)  # encripta la contraseña de el usuario 

            # crearr ususario 
            User.objects.create(first_name=name, username=username, last_name=lastname, email=email, password=password_enc, is_staff=False) 

            messages.success(request, 'User created')
             
            
            # logear al usuario
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(request, user)
                return redirect('productos/')
            else:
                 pass
        else:       
            if valid_username is not None:
                messages.error (request, 'Usuario en uso')
               
            elif valid_email is not None:
                messages.error(request, 'Usuario en uso')
               
            else:
                messages.error(request, 'Error inesperado')
               

    else:pass

       


    return redirect('register/')
    

def login_user (request):
    
    if request.user.is_authenticated:
        return redirect('/productos/')
    else:
        return render(request,'logs/login.html' )


def logear (request):

    password = request.POST['password']
    username = request.POST['username']

    
    user = authenticate(request, username=username, password=password) 

    if user is not None:
        messages.success(request, 'authenticated user')
        login( request, user )
    else:
        return redirect('login/')
     

    return redirect('productos/')


def user_detail(request, id):

    
    user = User.objects.filter(id=id).first()
    user_aut = request.user

    user_id = request.user.id

    context = {}

    if user_aut.is_authenticated:

        context = {
            'name':user.first_name,
            'lastname': user.last_name,
            'email': user.email,
            'username': user.username,
            'userrq': id,
            'userath':user_id
        }

    return render(request, 'user_detail.html', context)


@login_required 
def update (request , id ):

    if id != request.user.id:
        
        return redirect('/productos/')

    # No uso el get() por que si algo sale mal el filter solo retorna un none
    # pero el get me saca un error 
    user = User.objects.filter(id=id).first()
        
    return render(request, 'edit.html' ,{'user':user})


@login_required
def update_user (request, id):

    name = request.POST['name']
    last = request.POST['lastname']

    

    user = User.objects.filter(id=id).first()

    user.first_name = name
    user.last_name = last
    user.save()


    url = '/user/'+str(id)


    return redirect(url)
    

@login_required
def log_out (request):

    logout(request)


    return redirect('/')
    

def user_seacher(request):

    name =request.GET['seach']

    user = User.objects.filter(username=name).first()
    product = Product.objects.filter(name=name).first()
   
    if user is not None:

        uri =  '/user/' + str(user.id)
        
        return redirect (uri)
    elif product is not None:
        
        uri =  '/productos/' + str(product.id)

        return redirect (uri)
        
    return redirect('/')

@login_required
def user_deleter(request, id):
   
    if request.user.id == id: 

        user_ =  User.objects.filter( id=id ).first()

        logout(request)

        user_.delete()

        return redirect('/')
    
    return('productos/')


