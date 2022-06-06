from django.db import models

class Ciudadano(models.Model):
    nombre = models.CharField(max_length=40)
    documento = models.IntegerField()

class Desecho(models.Model):
    tipo = models.CharField(max_length=40)
    fechaDeIngreso = models.DateField()
    reciclable = models.BooleanField()
    peso = models.FloatField()

class Ticket(models.Model):
    ticketid = models.IntegerField()
    fechaDeEmision = models.DateField()
    monto = models.IntegerField()

class Estacion(models.Model):
    localidad = models.CharField(max_length=40)
    unidadNumero = models.IntegerField()