from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView
from .forms import (CustomMensajeroCreationForm, 
                    CustomAuthenticationForm, 
                    CustomClienteCreationForm, 
                    UpdateUserForm, 
                    UserFilter)


from .models import CustomUser, Mensajero
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse




class notAuthenticatedMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('/') 



class ClienteRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_cliente

class MensajeroRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_mensajero
    
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff



class MensajeroCreateView(notAuthenticatedMixin, CreateView):
    model = CustomUser
    form_class = CustomMensajeroCreationForm
    template_name = 'users/crearUsu.html'
    success_url = reverse_lazy('indexMensajero')  

    def form_valid(self, form):
        print(form.cleaned_data)
        response = super().form_valid(form)
        return response
    

class ClienteCreateView(notAuthenticatedMixin, CreateView):
    model = CustomUser
    form_class = CustomClienteCreationForm
    template_name = 'users/crearCliente.html'
    success_url = reverse_lazy('indexCliente')  

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
        elif user.is_staff:
            return reverse_lazy('indexAdmin')       
        else:
            return reverse_lazy('default_dashboard')  



class indexMensajeroTemplateView(MensajeroRequiredMixin, TemplateView):
    template_name = "users/indexMensajero.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['mensajero'] = Mensajero.objects.get(user = self.request.user.id)
        # context['placaformateada'] = Mensajero.formatted_placa() if Mensajero else None
        return context
    
class indexAdminTemplateView(AdminRequiredMixin, TemplateView):
    template_name = "admin/indexAdmin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['mensajero'] = Mensajero.objects.get(user = self.request.user.id)
        # context['placaformateada'] = Mensajero.formatted_placa() if Mensajero else None
        return context
    

class indexClienteTemplateView(ClienteRequiredMixin, TemplateView):
    template_name = "users/indexCliente.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['mensajero'] = Mensajero.objects.get(user = self.request.user.id)
        # context['placaformateada'] = Mensajero.formatted_placa() if Mensajero else None
        return context



class ListUserView(AdminRequiredMixin, ListView):
    model = CustomUser
    template_name = 'admin/listarUsuarios.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        queryset = CustomUser.objects.clientes()
        form = UserFilter(self.request.GET)
        if form.is_valid():
            tipo = form.cleaned_data.get('tipo')
            nombre = form.cleaned_data.get('nombre')
            ciudad = form.cleaned_data.get('ciudad')
            queryset = CustomUser.objects.clientes(nombre=nombre, tipo=tipo, ciudad=ciudad)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserFilter(self.request.GET or None) 
        return context


def logout_view(request):
    logout(request)
    return redirect('/')
    

class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = "users/updateUser.html"
    form_class =  UpdateUserForm
    # success_url = reverse_lazy('index')
    
    def get_success_url(self):
        return reverse_lazy('home_app:index')

    
        
