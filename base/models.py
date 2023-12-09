from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    
    
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rooms_as_host')
    responsableDiagnostico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rooms_as_diagnostic_responsible')
    responsableReparacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rooms_as_repair_responsible')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    fechaInsgreso = models.DateField()
    ingresodiaLaboral = models.BooleanField()
    fechaingLocal = models.DateField()
    codigoQr = models.CharField(max_length=200)
    reingreso = models.BooleanField()
    fotoDelantera = models.ImageField()
    fotoTrasera = models.ImageField()
    fotoSticker = models.ImageField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    pulgadas = models.IntegerField()
    codModelo = models.CharField(max_length=150)
    descripcionModelo = models.TextField(null=True, blank=True)
    condicion = models.CharField(max_length=100)
    fechaSticker = models.DateField()
    nombreSticker = models.CharField(max_length=100)
    codigoSticker = models.FloatField(null=True, blank=True)
    garantia = models.CharField(max_length=50)
    inicioDiagnostico = models.DateTimeField()
    diagnosticoTecnico = models.TextField(null=True, blank=True)
    presupuestado = models.BooleanField()
    description = models.TextField(null=True, blank=True)
    estadoPresupuesto = models.CharField(max_length=50)
    fechaAprobacion = models.DateField()
    inicioReparacion = models.DateTimeField()
    tipoReparacion = models.CharField(max_length=50)
    capUsado = models.CharField(max_length=100)
    bujes = models.CharField(max_length=100)
    repuestosUsados = models.TextField(null=True, blank=True)
    motor = models.CharField(max_length=50)
    codMotor = models.CharField(max_length=100)
    finalReparacion = models.DateTimeField()
    resumenGeneral = models.TextField(null=True, blank=True)
    fechaSalida = models.DateField()
    fotoSalida = models.ImageField()
    estadoActual = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.body[:50]
