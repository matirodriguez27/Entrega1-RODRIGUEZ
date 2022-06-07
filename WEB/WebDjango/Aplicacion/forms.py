from django import forms

class IngresoUsuario(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    socio = forms.IntegerField()

class NuevaAparicion(forms.Form):
    descripcionLugar = forms.CharField()
    superhumano = forms.CharField()
    huboHeridos = forms.BooleanField()