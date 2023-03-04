from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    name =  models.CharField( max_length=30 ,null=False, unique=True)
    create_at = models.DateTimeField( auto_now=True)
    def __str__(self) -> str:
        return self.name 

    class Meta:
        verbose_name_plural = "Categories" 

    
class Product(models.Model):
    name = models.CharField(max_length=30, null= False, unique=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.CharField(max_length=120, null=False)
    image = models.ImageField(upload_to='photos', null=True)
    cantidad = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    create_at = models.DateTimeField( auto_now=True)
   
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Products" 


class Talla(models.Model):
    talla =  models.CharField( max_length=30 ,null=False, unique=True)
    create_at = models.DateTimeField( auto_now=True)
    product = models.ManyToManyField(Product,through='Talla_product')
    def __str__(self) -> str:
        return self.talla

    class Meta:
        verbose_name_plural = "Tallas" 

class Color (models.Model):
    color =  models.CharField( max_length=30 ,null=False, unique=True)
    create_at = models.DateTimeField( auto_now=True)
    product = models.ManyToManyField(Product,through='Color_product')
    def __str__(self) -> str:
        return self.color

    class Meta:
        verbose_name_plural = "Colors" 


class Color_product (models.Model):
    
    color = models.ForeignKey(Color , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
     
    create_at = models.DateTimeField( auto_now=True)
    def __str__(self) -> str:
        return str(self.product) +' ' + str(self.color)

    class Meta:
        verbose_name_plural = "Colors_Products" 


class Talla_product (models.Model):
    
    talla = models.ForeignKey(Talla , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
     
    create_at = models.DateTimeField( auto_now=True)

    def __str__(self) -> str:
        return str(self.product )+ ' ' + str(self.talla)

    class Meta:
        verbose_name_plural = "Tallas_Products" 




     