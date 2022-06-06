from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse('vista inicio')
def estaciones(request):
    return HttpResponse('vista estaciones')
def ciudadanos(request):
    return HttpResponse('vista ciudadanos')
def desechos(request):
    return HttpResponse('vista desechos')
def tickets(request):
    return HttpResponse('vista tickets')