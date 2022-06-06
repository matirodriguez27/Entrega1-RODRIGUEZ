from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "Aplicacion/index.html")
def nuevoDesecho(request):
    return render(request, "Aplicacion/desechos.html")
