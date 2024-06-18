from django.urls import path
from .views import (MensajeroCreateView, 
                    CustomLoginView, 
                    indexMensajeroTemplateView, 
                    ClienteCreateView, 
                    indexClienteTemplateView,
                    logout_view,
                    UserUpdateView,
                    indexAdminTemplateView,
                    ListUserView)

urlpatterns = [
    path('create-mensajero/', MensajeroCreateView.as_view(), name='create_mensajero'),
    path('create-cliente/', ClienteCreateView.as_view(), name='create_cliente'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('indexMensajero/', indexMensajeroTemplateView.as_view(), name='indexMensajero'),
    path('indexCliente/', indexClienteTemplateView.as_view(), name='indexCliente'),
    path('indexAdmin/', indexAdminTemplateView.as_view(), name='indexAdmin'),
    path('listUser/', ListUserView.as_view(), name='listUser'),
    path('updateUser/<int:pk>/', UserUpdateView.as_view(), name='updateUser'),
    path('logout/', logout_view, name='logout'),
    # Otras rutas...
]