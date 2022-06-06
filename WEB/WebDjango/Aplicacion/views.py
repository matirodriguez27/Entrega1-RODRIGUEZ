from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "Aplicacion/inicio.html")
def estaciones(request):
    return render(request, "Aplicacion/estaciones.html")
def ciudadanos(request):
    return render(request, "Aplicacion/ciudadanos.html")
def desechos(request):
    return render(request, "Aplicacion/desechos.html")
def tickets(request):
    return render(request, "Aplicacion/tickets.html")