from django.shortcuts import render,redirect
from products.models import Product
from  django.contrib.auth.models import User

from . import models

# Create your views here.

def fedback (request, id):
     
     text= request.POST['text']
      
     product = Product.objects.filter(id=id).first()

     user = User.objects.filter(id=request.user.id).first()

     comment = models.Comment.objects.create(comment=text , user= user,  product=product )

     return redirect('/productos/'+str(id))