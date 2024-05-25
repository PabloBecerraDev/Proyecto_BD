from django.contrib.auth.models import BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager, models.Manager):
    def create_user(self, username, direccion, email, telefono, identificacion, imagenPerfil, password=None, is_staff=False, is_superuser=False, **extra_fields):
        if not username:
            raise ValueError('El nombre de usuario debe ser proporcionado')
        if not direccion:
            raise ValueError('La dirección debe ser proporcionada')
        if not telefono:
            raise ValueError('El teléfono debe ser proporcionado')
        if not identificacion:
            raise ValueError('La identificación debe ser proporcionada')

        user = self.model(
            username=username,
            direccion=direccion,
            email = email,
            telefono=telefono,
            identificacion=identificacion,
            imagenPerfil = imagenPerfil,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # esta es una funcion para crear mensajero reciviendo todos sus atributos, como tal no se usa por que los creamos desde
    # el form
    def create_mensajero(self, username, direccion, telefono, identificacion, vehiculo, password=None):
        extra_fields = {
            'is_cliente': False,
            'is_mensajero': True,
        }
        user = self.create_user(username, direccion, telefono, identificacion, password, **extra_fields)
        
        from .models import Mensajero
        Mensajero.objects.create(user=user, vehiculo=vehiculo)
        return user
    
    # def create_cliente(self, username, direccion, telefono, identificacion, ciudad, address, password=None):
    #     extra_fields = {
    #         'is_cliente': True,
    #         'is_mensajero': False,
    #     }
    #     user = self.create_user(username, direccion, telefono, identificacion, password, **extra_fields)
        
    #     from .models import Mensajero
    #     Mensajero.objects.create(user=user, vehiculo=vehiculo)
    #     return user
    
    def create_superuser(self, username, direccion="null", email="null", telefono="null", identificacion="null", password=None, **extra_fields):
        return self.create_user(username, direccion, email, telefono, identificacion, password, True, True, **extra_fields)