# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Cliente, Mensajero

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('is_cliente', 'is_mensajero')

class ClienteProfileForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['address']

class MensajeroProfileForm(forms.ModelForm):
    class Meta:
        model = Mensajero
        fields = ['vehiculo']






from django import forms
from .models import CustomUser, Mensajero

# class CustomUserCreationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'direccion', 'telefono', 'identificacion']  # Excluir 'is_cliente' e 'is_mensajero'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['direccion'].required = True
#         self.fields['telefono'].required = True
#         self.fields['identificacion'].required = True
#         self.fields['username'].required = True


#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         user.is_cliente = False  # Asegurarse de que no sea cliente
#         user.is_mensajero = True  # Marcar como mensajero

#         if commit:
#             user.save()

#             # Si se proporciona un vehículo, crear el mensajero
#             vehiculo = self.cleaned_data.get('vehiculo')
#             if vehiculo:
#                 Mensajero.objects.create(user=user, vehiculo=vehiculo)

#         return user




class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    vehiculo = forms.ChoiceField(choices=Mensajero.VEHICULO_CHICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'direccion', 'telefono', 'identificacion', 'vehiculo']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['direccion'].required = True
        self.fields['telefono'].required = True
        self.fields['identificacion'].required = True
        self.fields['username'].required = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_cliente = False  
        user.is_mensajero = True  

        if commit:
            user.save()
            vehiculo = self.cleaned_data['vehiculo']
            Mensajero.objects.create(user=user, vehiculo=vehiculo)

        return user
    
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    #prueba2 - 1234
