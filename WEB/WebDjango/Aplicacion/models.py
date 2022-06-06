from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    idUsuario = models.IntegerField(primary_key=True)

class Desecho(models.Model):
    tipo = models.CharField(max_length=40)
    fechaDeIngreso = models.DateField()
    peso = models.FloatField()
    usuarioAsociado = models.IntegerField

class Ticket(models.Model):
    idTicket = models.IntegerField(primary_key=True)
    fechaDeEmision = models.DateField()
    monto = models.IntegerField()
    usuarioAsociado = models.IntegerField()

class Estacion(models.Model):
    localidad = models.CharField(max_length=40)
    idEstacion = models.IntegerField(primary_key=True)