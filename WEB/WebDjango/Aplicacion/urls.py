from django.urls import path, include
from Aplicacion import views

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('nuevaAparicion', views.nuevaAparicion, name = "nuevaAparicion"),
    path('nuevoUsuario', views.nuevoUsuario, name = "nuevoUsuario"),
    path('buscarUsuario', views.buscarUsuario, name = "buscarUsuario"),
    path('buscarAparicion', views.buscarAparicion, name = "buscarAparicion"),
    path('buscar/', views.buscar)
]