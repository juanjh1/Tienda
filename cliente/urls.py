from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register , name="register"),
    path("login/", views.login_user , name="login"),
    path("createUser", views.Create_user, name='createuser' ),
    path("log", views.logear , name='log'),
    path("user/<int:id>", views.user_detail, name='user_detail'),
    path("user/<int:id>/update", views.update, name='update_user'),
    path("user/<int:id>/update/up", views.update_user, name='update'),
    path('logout/', views.log_out, name='logout'),
    path('userseach/' , views.user_seacher, name='userseach'),
    path("user/<int:id>/delete/", views.user_deleter, name='delete_user')
]
