from django import forms

class NuevaAparicion(forms.Form):
    descripcionLugar = forms.CharField()
    superhumano = forms.CharField()
    huboHeridos = forms.BooleanField()