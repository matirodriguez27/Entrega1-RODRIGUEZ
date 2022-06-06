from django.urls import path, include
from Aplicacion import views

urlpatterns = [
    path('', views.inicio),
    path('estaciones', views.estaciones),
    path('ciudadanos', views.ciudadanos),
    path('desechos', views.desechos),
    path('tickets', views.tickets),
]