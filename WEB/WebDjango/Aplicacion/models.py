from django.db import models

class Superhumano(models.Model):
    nombre = models.CharField(max_length=40)
    nivelDePoder = models.IntegerField()
    idSuperhumano = models.IntegerField(primary_key=True)
    esMalvado = models.BooleanField()

class Organizacion(models.Model):
    nombre = models.CharField(max_length=40)
    cantIntegrantes = models.IntegerField()

class Aparicion(models.Model):
    descripcionLugar = models.CharField(max_length=100)
    superhumano = models.CharField(max_length=20)
    huboHeridos = models.BooleanField()
