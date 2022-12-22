from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields
from django.forms.forms import Form
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

        
class ResgistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Correo',
        }

class ResetPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese un username',
        'class': 'form-cpntrol',
        'autocomplete': 'off'
    }))

    


class PostForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'teaser', 'contenido', 'imagen', 'categoria', 'usuario']