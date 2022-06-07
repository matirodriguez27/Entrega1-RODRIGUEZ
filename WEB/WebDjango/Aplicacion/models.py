from django.db import models

class Superhumano(models.Model):
    nombre = models.CharField(max_length=40)
    nivelDePoder = models.IntegerField()
    idSuperhumano = models.IntegerField(primary_key=True)

class Organizacion(models.Model):
    nombre = models.CharField(max_length=40)
    cantIntegrantes = models.IntegerField()

class Aparicion(models.Model):
    superhumano = models.CharField(max_length=20)
    descripcionLugar = models.CharField(max_length=100)
