from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.forms import Form
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'teaser', 'contenido', 'imagen', 'categoria', 'usuario']


class ContactForm(forms.Form):
    Nombre = forms.CharField(max_length=50)
    Apellido = forms.CharField(max_length=50)
    Correo_Electronico = forms.EmailField(max_length=150)
    Mensaje = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), max_length=2000)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class Coment(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    texto = models.TextField(max_length = 1500)
    noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.noticia}->{self.texto}"


    
