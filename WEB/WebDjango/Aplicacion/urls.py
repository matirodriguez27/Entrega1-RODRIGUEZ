from django.urls import path, include
from Aplicacion import views

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('nuevoUsuario', views.nuevoUsuario, name = "nuevoUsuario"),
    path('buscarUsuario', views.buscarUsuario, name = "buscarUsuario"),
    path('buscar/', views.buscar)
]