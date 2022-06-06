from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from Aplicacion.forms import IngresoUsuario
from Aplicacion.models import Usuario

# Create your views here.
def inicio(request):
    return render(request, "Aplicacion/inicio.html")

def nuevoUsuario(request):
    if request.method == 'POST':
        miFormulario = IngresoUsuario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            usuario = Usuario(nombre = informacion['nombre'], email=informacion['email'], idUsuario = informacion['socio'])
            usuario.save()
            return render(request, "Aplicacion/nuevoUsuario.html")
    else:
            miFormulario = IngresoUsuario()

    return render(request, "Aplicacion/nuevoUsuario.html", {"miFormulario":miFormulario})
def buscarUsuario(request):

    return render(request, "Aplicacion/buscarUsuario.html")

def buscar(request):
    if request.GET["socio"]:
        socio = request.GET["socio"]
        usuarios = Usuario.objects.filter(idUsuario__icontains=socio)
        return render(request, "Aplicacion/resultadosBusquedaUsuario.html", {"socio":socio,"usuarios":usuarios})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)