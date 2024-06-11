from django.urls import path
from .views import MensajeroCreateView, CustomLoginView, indexMensajeroTemplateView, ClienteCreateView, indexClienteTemplateView

urlpatterns = [
    path('create-mensajero/', MensajeroCreateView.as_view(), name='create_mensajero'),
    path('create-cliente/', ClienteCreateView.as_view(), name='create_cliente'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('indexMensajero/', indexMensajeroTemplateView.as_view(), name='indexMensajero'),
    path('indexCliente/', indexClienteTemplateView.as_view(), name='indexCliente'),
    # Otras rutas...
]