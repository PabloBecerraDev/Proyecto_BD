# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Cliente, Mensajero

# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.is_cliente:
#             Cliente.objects.create(user=instance)
#         if instance.is_mensajero:
#             Mensajero.objects.create(user=instance)


# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.is_cliente:
#         instance.cliente.save()
#     if instance.is_mensajero:
#         instance.mensajero.save()
