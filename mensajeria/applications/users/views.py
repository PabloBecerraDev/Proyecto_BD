from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser, Mensajero
from django.contrib.auth.mixins import LoginRequiredMixin

class MensajeroCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/crearUsu.html'
    success_url = reverse_lazy('mensajero_list')  

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = CustomAuthenticationForm


class indexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "users/indexMensajero.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensajero'] = Mensajero.objects.get(user = self.request.user.id)
        return context
    

