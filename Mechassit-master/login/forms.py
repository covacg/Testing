from django import forms
from .models import ExtendedData, Vehiculos
from .models import Servicios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


class AuthenticationuseUserForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']

class createUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']    

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = ExtendedData
        fields = "__all__"
        widgets = {
            'direccion': forms.TextInput(attrs={'required': False}),
            'cp': forms.TextInput(attrs={'required': False}),
            'calidad': forms.NumberInput(attrs={'required': False}),
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = ['tipo', 'modelo', 'año']

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ['tipo', 'tiempo', 'precio']

class UserEditForm(forms.ModelForm):
    telefono = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = ['email', 'telefono']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        if self.instance:
            extended_data = ExtendedData.objects.filter(user=self.instance).first()
            if extended_data:
                self.fields['telefono'].initial = extended_data.telefono