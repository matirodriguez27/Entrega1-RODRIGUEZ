from django import forms

class NuevaAparicion(forms.Form):
    descripcionLugar = forms.CharField()
    superhumano = forms.CharField()

class NuevoHeroe(forms.Form):
    nombre = forms.CharField()
    poder = forms.IntegerField()

class NuevaOrganizacion(forms.Form):
    nombre = forms.CharField()
    cantIntegrantes = forms.IntegerField()
