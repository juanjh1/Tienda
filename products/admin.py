from django.contrib import admin
from . import models
from .models import Product
# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Color)
admin.site.register(models.Product)
admin.site.register(models.Talla)
admin.site.register(models.Color_product)
admin.site.register(models.Talla_product)




class AlbumImageInline(admin.TabularInline):
    model = Product
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    inlines = [ AlbumImageInline ]