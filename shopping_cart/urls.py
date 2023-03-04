from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.car , name='shopping'),
    path('add/<int:id>' , views.add_car_template, name= 'add_product'),
    path('add/<int:id>/product' , views.add_car, name= 'add'),
    path('<int:id>/delete' , views.delete_item, name= 'delete_item'),
    
]
