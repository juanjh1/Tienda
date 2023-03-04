from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products , name='products'),
    path('<int:id>', views.detail_product, name='detail_products'),
    path('create/', views.create_product, name='create_product'),
    path('create/product', views.create, name='create'),
    path('mi/<int:id>' , views.my_products , name= 'my_products'),
    path('mi/<int:id>/delete' , views.delete_product , name= 'delete_product'),
     path('mi/<int:id>/update' , views.update , name= 'update_product'),
    
    
    
]
