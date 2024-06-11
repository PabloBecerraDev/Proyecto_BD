from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser, PermissionsMixin):
    is_cliente = models.BooleanField(default=False)
    is_mensajero = models.BooleanField(default=False)
    nombres = models.CharField(max_length = 100, blank = True)
    apellidos = models.CharField(max_length = 100, blank = True)
    username = models.CharField(max_length = 25, unique = True)
    direccion = models.CharField(max_length = 60, blank=True, default = "NULL")
    email = models.EmailField(unique=False)
    telefono = models.CharField(max_length = 20, blank=True, default = "NULL")
    identificacion = models.CharField(max_length = 20)
    imagenPerfil = models.ImageField(upload_to='perfil_imagenes/', blank=False, null=True)
    

    CIUDAD_CHOICES = (
        ('C','Santiago de Cali'),
        ('B','Bogota'),
        ('M','Medellin'),
        ('P','Pereira'),
    )

    ciudad = models.CharField(max_length = 100, choices = CIUDAD_CHOICES)

    #se pueden poner funciones aca normal 

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Cliente(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    nombreSucursal = models.CharField(max_length=255, blank = True)
    telefonoSucursal = models.CharField(max_length = 20, blank = True)
    

    def __str__(self):
        return self.user.username


class Mensajero(models.Model):

    VEHICULO_CHOICES = (
        ('M','Moto'),
        ('C','Carro'),
        ('F','Camion'),
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    vehiculo = models.CharField(max_length=1 , choices = VEHICULO_CHOICES, blank = True)
    placaVehiculo = models.CharField(max_length = 6, blank = True)

    def __str__(self):
        return self.user.username
    
    def placaFormato(self):
        if len(self.placaVehiculo) == 6:
            return f"{self.placaVehiculo[:3]}-{self.placaVehiculo[3:]}"
        return self.placaVehiculo 