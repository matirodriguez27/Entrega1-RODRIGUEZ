from django import forms

class IngresoUsuario(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    socio = forms.IntegerField()