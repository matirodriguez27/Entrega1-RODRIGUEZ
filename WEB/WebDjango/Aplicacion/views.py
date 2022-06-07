from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from Aplicacion.forms import IngresoUsuario,NuevaAparicion
from Aplicacion.models import Usuario, Aparicion

# Create your views here.
def inicio(request):
    return render(request, "Aplicacion/inicio.html")

def nuevaAparicion(request):
    if request.method == 'POST':
        miFormulario = NuevaAparicion(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            aparicion = Aparicion(descripcionLugar = informacion['descripcionLugar'], superhumano=informacion['superhumano'], huboHeridos = informacion['huboHeridos'])
            aparicion.save()
            return render(request, "Aplicacion/nuevaAparicion.html")
    else:
            miFormulario = NuevaAparicion()

    return render(request, "Aplicacion/nuevaAparicion.html", {"miFormulario":miFormulario})

def buscarAparicion(request):
    return render(request, "Aplicacion/buscarAparicion.html")

def buscar(request):
    if request.GET["socio"]:
        heroe = request.GET["superhumano"]
        apariciones = Aparicion.objects.filter(superhumano__icontains=heroe)
        return render(request, "Aplicacion/resultadosBusquedaAparicion.html", {"superhumano":heroe,"apariciones":apariciones})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)