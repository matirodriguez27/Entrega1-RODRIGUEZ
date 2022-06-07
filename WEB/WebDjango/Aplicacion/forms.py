from django import forms

class NuevaAparicion(forms.Form):
    descripcionLugar = forms.CharField()
    superhumano = forms.CharField()
    huboHeridos = forms.BooleanField()

class NuevoHeroe(forms.Form):
    nombre = forms.CharField()
    nivelDePoder = forms.IntegerField()
    idSuperhumano = forms.IntegerField()
    esMalvado = forms.BooleanField()

class NuevaOrganizacion(forms.Form):
    nombre = forms.CharField()
    cantIntegrantes = forms.IntegerField()
