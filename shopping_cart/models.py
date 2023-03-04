
from django.db import models
from django.contrib.auth.models import User
from products.models import Product, Color, Talla

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.usuario) +' ' +str(self.id)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def subtotal(self):
        return self.cantidad * self.precio
    
    def __str__(self) -> str:
        return str(self.carrito) +' ' +str(self.producto)