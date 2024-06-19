from django.db import models
from django.conf import settings
import requests
from django.core.exceptions import ValidationError
from applications.users.models import CustomUser
from .managers import ManajerServicios

# Create your models here.

class Direccion(models.Model):
    direccion = models.CharField(max_length=300)
    CIUDAD_CHOICES = (
        ('C','Santiago de Cali'),
        ('B','Bogota'),
        ('M','Medellin'),
        ('P','Pereira'),
    )
    ciudad = models.CharField(max_length=100, choices=CIUDAD_CHOICES)
    departamento = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    pais = models.CharField(max_length=100)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        return f'{self.direccion}, {self.ciudad}, {self.departamento}, {self.pais}, {self.codigo_postal}'

    def get_lat_long_google(address, city, country, department, api_key):
        full_address = f"{address}, {city}, {department}, {country}"
        geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={full_address}&key={api_key}"
        
        # Imprimir la URL para depuración
        print(f"URL de geocodificación: {geocoding_url}")
        
        response = requests.get(geocoding_url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Imprimir la respuesta JSON para depuración
            print(f"Respuesta JSON: {data}")
            
            if data['results']:
                location = data['results'][0]['geometry']['location']
                return location['lat'], location['lng']
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
        
        return None, None

    def save(self, *args, **kwargs):
        if not self.latitud or not self.longitud:
            address = f'{self.direccion}, {self.get_ciudad_display()}, {self.departamento}, {self.pais}'
            api_key = 'AIzaSyDIsLYWRxE2ME1PBLk1ugSZvu8OLfoAuKE'
            geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
            
            # Realiza la solicitud a la API de Google Maps
            response = requests.get(geocoding_url)
            if response.status_code == 200:
                result = response.json()
                if result['status'] == 'OK':
                    self.latitud = result['results'][0]['geometry']['location']['lat']
                    self.longitud = result['results'][0]['geometry']['location']['lng']
            else:
                raise ValidationError('Error al contactar con la API de Google Maps.')

        # Llama al método save original para guardar el objeto
        super().save(*args, **kwargs)

class Servicio(models.Model):
    id_cliente = models.ForeignKey(CustomUser, 
                                   on_delete=models.CASCADE, 
                                   related_name='servicios_cliente', 
                                   blank=False, 
                                   null=False)
    id_mensajero = models.ForeignKey(CustomUser, 
                                     on_delete=models.CASCADE, 
                                     related_name='servicios_mensajero', 
                                     blank=True, 
                                     null=True)
    
    VEHICULO_CHICES = (
        ('M','Moto'),
        ('C','Carro'),
        ('F','Camion'),
    )

    cantidadPaquetes = models.BigIntegerField(blank = True, null = True)

    vehiculoSolicitado = models.CharField(max_length=1 , choices = VEHICULO_CHICES, blank = True)
    direccion_recojer = models.ForeignKey(Direccion, on_delete = models.CASCADE, related_name = 'direccion1', blank = False, null = False)
    direccion_destino = models.ForeignKey(Direccion, on_delete = models.CASCADE, related_name = 'direccion2', blank = False, null = False)
    SERVICIO_ESTADOS = (
        ('S', 'Solicitado.'),
        ('A', 'Agendado, un mensajero tomo tu pedido.'),
        ('C', 'Tu envío está en camino.'),
        ('D', 'Tu envío ha llegado a su destino.'),
        ('E', 'Tu envío ha sido entregado.'),
    )
    estados = models.CharField(max_length=1, choices=SERVICIO_ESTADOS, blank=True)

    def getEstado(self):
        return self.get_estados_display()


    descripcion = models.CharField(max_length=300, null=False, blank=False)
    is_complete = models.BooleanField(blank = True, null = True, default = False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)


    objects = models.Manager()  
    servicios_cliente = ManajerServicios()  


    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):  
        return f'Servicio {self.id} - {self.descripcion}'