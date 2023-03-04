from django.shortcuts import render, redirect
from .models import Carrito, ItemCarrito
from products.models import Product, Talla, Color
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def car (request):
    context={}
    carrito = Carrito.objects.filter(usuario=request.user.id).first()
    if carrito is not None:

        items = ItemCarrito.objects.filter(carrito=carrito)
        total = 0
        for item in items:

            total += int(item.precio) *int(item.cantidad) 

        context={'items':items,
                 'total':total}
    
        
        return render(request, 'shoping.html',context )
    
      
    else:
         Carrito.objects.create(usuario=request.user)

         return redirect('/shoping/')



login_required
def add_car_template(request,id):
    
    product_add = Product.objects.filter(id=id).first

    if product_add is not None:
       

       context  = {'product_add':product_add,
                   'tallas':Talla.objects.all(),
                    'colors':Color.objects.all()}
        
       return render(request, 'add.html',context)
    else:
        messages.error (request, '')
        return redirect('/productos/')
    
login_required
def  add_car (request,id):

    user_car = Carrito.objects.filter(usuario=request.user.id).first()
    cantidad = request.POST['product_quantity']
    precio  = request.POST['product_price']
    talla = request.POST['talla']
    color = request.POST['color']

    product = Product.objects.filter(id=id).first()
    talla = Talla.objects.filter(id=int(talla)).first()
    color = Color.objects.filter(id=int(color)).first()

    print(talla, color)
    if int(product.cantidad ) > int(cantidad) :

        ItemCarrito.objects.create(carrito=user_car, producto=product, cantidad=cantidad, precio = precio, talla=talla, color=color)

        product.cantidad =  int(product.cantidad) - int(cantidad)
        product.save()

        messages.success(request, 'Item added successfully') 
        
        return redirect('/productos/')
        
    else: 
        messages.error(request, 'Quantity not available') 
        return redirect('/productos/')

login_required
def delete_item(request, id):
    
    item = ItemCarrito.objects.filter(id=id).first()

    carrito = Carrito.objects.filter(id=item.carrito.id).first()

    if carrito.usuario.id == request.user.id:

        item.delete()
        messages.success(request, 'your items is deteled')
    else:
        messages.error(request, 'you dont have the necessary permissions' )
    return redirect('/shoping/')