from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .forms import CustomMensajeroCreationForm, CustomAuthenticationForm, CustomClienteCreationForm
from .models import CustomUser, Mensajero
from django.contrib.auth.mixins import LoginRequiredMixin

class MensajeroCreateView(CreateView):
    model = CustomUser
    form_class = CustomMensajeroCreationForm
    template_name = 'users/crearUsu.html'
    success_url = reverse_lazy('mensajero_list')  

    def form_valid(self, form):
        print(form.cleaned_data)
        response = super().form_valid(form)
        return response
    

class ClienteCreateView(CreateView):
    model = CustomUser
    form_class = CustomClienteCreationForm
    template_name = 'users/crearCliente.html'
    success_url = reverse_lazy('mensajero_list')  

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        user = self.request.user
        if user.is_cliente:
            return reverse_lazy('indexCliente')  
        elif user.is_mensajero:
            return reverse_lazy('indexMensajero')
        # elif user.is_staff:
        #     return reverse_lazy('indexAdmin')  
        else:
            return reverse_lazy('default_dashboard')  



class indexMensajeroTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "users/indexMensajero.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['mensajero'] = Mensajero.objects.get(user = self.request.user.id)
        # context['placaformateada'] = Mensajero.formatted_placa() if Mensajero else None
        return context
    

class indexClienteTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "users/indexCliente.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['mensajero'] = Mensajero.objects.get(user = self.request.user.id)
        # context['placaformateada'] = Mensajero.formatted_placa() if Mensajero else None
        return context
    

