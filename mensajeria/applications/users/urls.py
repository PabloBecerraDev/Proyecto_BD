from django.urls import path
from .views import MensajeroCreateView, CustomLoginView, indexTemplateView, ClienteCreateView

urlpatterns = [
    path('create-mensajero/', MensajeroCreateView.as_view(), name='create_mensajero'),
    path('create-cliente/', ClienteCreateView.as_view(), name='create_cliente'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('log/', indexTemplateView.as_view(), name='log'),
    # Otras rutas...
]