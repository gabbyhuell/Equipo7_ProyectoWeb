from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields
from django.forms.forms import Form
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'teaser', 'contenido', 'imagen', 'categoria', 'usuario']

class ContactForm(forms.Form):
	Nombre = forms.CharField(max_length = 50)
	Apellido = forms.CharField(max_length = 50)
	Correo_Electronico = forms.EmailField(max_length = 150)
	Mensaje = forms.CharField(widget = forms.Textarea, max_length = 2000)