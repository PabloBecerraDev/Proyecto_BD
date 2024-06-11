# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Cliente, Mensajero



class CustomClienteCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    ciudad = forms.Select(attrs={'class': 'form-control'})
    nombreSucursal = forms.CharField(widget = forms.TextInput, required = True)
    telefonoSucursal = forms.CharField(widget = forms.TextInput, required = True)

    class Meta:
        model = CustomUser
        fields = ['username', 
                  'nombres',
                  'apellidos',
                  'direccion', 
                  'telefono', 
                  'identificacion', 
                  'email', 
                  'imagenPerfil', 
                  'ciudad', 
                  'nombreSucursal',
                  'telefonoSucursal',
                  ]  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['direccion'].required = True
        self.fields['email'].required = True
        self.fields['telefono'].required = True
        self.fields['identificacion'].required = True
        self.fields['username'].required = True
        self.fields['imagenPerfil'].required = False

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_cliente = True  # Asegurarse de que no sea cliente
        user.is_mensajero = False  # Marcar como mensajero

        if commit:
            user.save()
            ciudad = self.cleaned_data.get('ciudad')
            nombreSucursal = self.cleaned_data.get('nombreSucursal')
            telefonoSucursal = self.cleaned_data.get('telefonoSucursal')
            if ciudad:
                Cliente.objects.create(user=user, nombreSucursal = nombreSucursal, telefonoSucursal = telefonoSucursal )

        return user







class CustomMensajeroCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    vehiculo = forms.ChoiceField(choices=Mensajero.VEHICULO_CHOICES, required=True)
    placaVehiculo = forms.CharField(widget = forms.TextInput, required=True)
    ciudad = forms.Select(attrs={'class': 'form-control'})
    imagenPerfil = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username','nombres', 'apellidos', 'direccion', 'telefono', 'identificacion', 
                  'email', 'vehiculo', 'placaVehiculo', 'imagenPerfil', 'ciudad',
                  ]  

    def __init__(self, *args, **kwargs):
        print("sii")
        super().__init__(*args, **kwargs)
        self.fields['direccion'].required = True
        self.fields['email'].required = True
        self.fields['telefono'].required = True
        self.fields['identificacion'].required = True
        self.fields['username'].required = True
        self.fields['imagenPerfil'].required = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_cliente = False  
        user.is_mensajero = True  

        if commit:
            print("guardando usuario")
            user.save()
            vehiculo = self.cleaned_data['vehiculo']
            placaVehiculo = self.cleaned_data['placaVehiculo']
            Mensajero.objects.create(user = user, vehiculo = vehiculo, placaVehiculo = placaVehiculo)
            
            if 'imagenPerfil' in self.cleaned_data and self.cleaned_data['imagenPerfil']:
                user.imagenPerfil = self.cleaned_data['imagenPerfil']
                user.save()
                print("imagen si proporcionada")
            else:
                print("imagen no proporcionada")

        return user


# este es el formulario para el Login
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    #prueba2 - 1234
