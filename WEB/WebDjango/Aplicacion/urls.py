from django.urls import path, include
from Aplicacion import views

urlpatterns = [
    path('', views.inicio),
    path('nuevoUsuario', views.nuevoUsuario),
]