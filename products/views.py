from django.shortcuts import render,redirect
from  django.contrib.auth.models import User
from . import models
from django.contrib.auth.decorators import login_required
from coments.models import Comment
from .form import ProductForm,TallaColorForm
from django.contrib import messages


# Create your views here.
def products (request):


    context = {
               'user': request.user, 
               'products':  models.Product.objects.all()
               }
    

    return render(request, 'products.html',context)



def detail_product(request, id):
   

    product = models.Product.objects.filter(id=id).first()

    context= {
              'product':product ,
              'colores':product.color_set.all(), 
              'tallas':product.talla_set.all(),
              'user_created':product.user.id ,
              'comments':Comment.objects.filter(product=id)
              }
    
    return render(request, 'detail_products.html',context )

@login_required
def create_product (request):

    context= {
               'form': ProductForm(),
               'talla_color': TallaColorForm()
             }
    return render(request, 'create_prod.html',context)


@login_required
def create (request):

    if request.method == 'POST':

        form = ProductForm(request.POST, files=request.FILES)
        form_talla_color = TallaColorForm(request.POST)
        
        if form.is_valid() and form_talla_color.is_valid(): 
            category = models.Category.objects.filter(id=1).first()
            user_ = User.objects.filter(id=request.user.id).first()

            new_product = form.save(commit=False)
            new_product.user = user_
            new_product.category = category
            new_product.save()

            tallas = form_talla_color.cleaned_data['tallas']
            colores = form_talla_color.cleaned_data['colores']

            for talla in tallas:
                new_product.talla_set.add(talla)
            for color in colores:
                new_product.color_set.add(color)
            
            messages.success(request,' Product created successfully')
    
            
            return redirect('/productos/')
        else:
            messages.error(request, form.errors)
      
    return redirect('/')
    

def my_products (request, id):

    
    context =  {'products':models.Product.objects.filter(user=id)}

    return render(request, 'my_products.html',context)



def delete_product(request , id):

    product = models.Product.objects.filter(id=id).first()


    if product.user.id == request.user.id:

        product.delete()

        messages.success(request, 'discontinued product')
    else:
        messages.error(request, 'producto si eliminar')

        
    return redirect('/productos/')


def update(request, id):
    product = models.Product.objects.filter(id=id).first()

    
    
    context ={
      'product':product
    }

    if request.method == 'POST':
        if product.user.id == request.user.id:

            desc = request.POST['desc']
            cantidad = request.POST['cantidad']
            price = request.POST['price']
            
            print(desc,cantidad,price)


            product.desc = desc
            product.cantidad = cantidad
            product.price = price

            product.save()

            return redirect('/productos/'+str(id))
    return render(request, 'edit_porduct.html',context, )