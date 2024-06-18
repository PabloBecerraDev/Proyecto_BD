from django.urls import path
from .views import( CrearServicioView, VerServiciosCliente, HistorialServiciosClienteView, ServiciosDisponiblesParaMensajeroView, AceptarServicioView, GestionarServicioView, CompletarServicioView, HistorialServiciosMensajeroView, ServicioListView)

app_name = "servicios_app"

urlpatterns = [
    path('crear-servicio/', CrearServicioView.as_view(), name='crear_servicio'),
    path('listar-servicio/', VerServiciosCliente.as_view(), name='listar_servicio'),
    path('historialCliente/', HistorialServiciosClienteView.as_view(), name='historialCliente'),
    path('seleccionarServicio/', ServiciosDisponiblesParaMensajeroView.as_view(), name = 'listar_servicios_mensajero'),
    path('aceptar-servicio/<int:servicio_id>/', AceptarServicioView.as_view(), name='aceptar_servicio'),
    path('gestionar-servicio/', GestionarServicioView.as_view(), name = 'gestionarServicio'),
    path('servicio/completar/', CompletarServicioView.as_view(), name='completarServicio'),
    path('historialMensajero/', HistorialServiciosMensajeroView.as_view(), name='historialMensajero'),
    path('listarServiciosAdmin/', ServicioListView.as_view(), name='admin_servicio_list'),
    
    #path('reporte/', generar_reporte, name='generar_reporte'),
]