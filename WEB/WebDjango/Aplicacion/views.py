from django.http import HttpResponse
from django.shortcuts import render
from Aplicacion.forms import NuevaAparicion, NuevoHeroe, NuevaOrganizacion
from Aplicacion.models import  Aparicion, Superhumano, Organizacion

# Create your views here.
def inicio(request):
    return render(request, "Aplicacion/inicio.html")

def nuevaAparicion(request):
    if request.method == 'POST':
        miFormulario = NuevaAparicion(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            aparicion = Aparicion(descripcionLugar = informacion['descripcionLugar'], superhumano=informacion['superhumano'])
            aparicion.save()
            return render(request, "Aplicacion/nuevaAparicion.html")
    else:
            miFormulario = NuevaAparicion()
    return render(request, "Aplicacion/nuevaAparicion.html", {"miFormulario":miFormulario})

def nuevoHeroe(request):
    if request.method == 'POST':
        miFormulario = NuevoHeroe(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            heroe = Superhumano(nombre = informacion['nombre'], poder=informacion['poder'])
            heroe.save()
            return render(request, "Aplicacion/nuevaAparicion.html")
    else:
            miFormulario = NuevoHeroe()
    return render(request, "Aplicacion/nuevoHeroe.html", {"miFormulario":miFormulario})

def nuevaOrganizacion(request):
    if request.method == 'POST':
        miFormulario = NuevaOrganizacion(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            organizacion = Organizacion(nombre = informacion['nombre'], cantIntegrantes=informacion['cantIntegrantes'])
            organizacion.save()
            return render(request, "Aplicacion/nuevaOrganizacion.html")
    else:
            miFormulario = NuevaOrganizacion()
    return render(request, "Aplicacion/nuevaAparicion.html", {"miFormulario":miFormulario})

def buscarAparicion(request):
    return render(request, "Aplicacion/buscarAparicion.html")

def buscar(request):
    if request.GET["superhumano"]:
        heroe = request.GET["superhumano"]
        apariciones = Aparicion.objects.filter(superhumano__icontains=heroe)
        return render(request, "Aplicacion/resultadosBusquedaApariciones.html", {"superhumano":heroe,"apariciones":apariciones})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)