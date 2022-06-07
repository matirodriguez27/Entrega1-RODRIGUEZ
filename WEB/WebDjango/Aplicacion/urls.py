from django.urls import path, include
from Aplicacion import views

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('nuevaAparicion', views.nuevaAparicion, name = "nuevaAparicion"),
    path('buscarAparicion', views.buscarAparicion, name = "buscarAparicion"),
    path('nuevoHeroe', views.nuevoHeroe, name = "nuevoHeroe"),
    path('nuevaOrganizacion', views.nuevaOrganizacion, name = "nuevaOrganizacion"),
    path('buscar/', views.buscar)
]