"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido),
    path('despedida.html', despedirse),
    path('nosotros.html', nosotros),
    path('index.html', inicio),
    path('registrarse.html', registrarse),
    path('login.html', login),
    path('crear_post.html', crearPost),
    path('busqueda.html', Busqueda),
    path('resultado.html', resultado),
    path("contacto.html", contact),
    path("trabajo.html", trabajo),
    path("a.html", b)
]
