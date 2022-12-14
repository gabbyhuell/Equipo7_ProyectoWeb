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
from django.urls import path, include
from webapp.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', inicio), 
    path('admin/', admin.site.urls),
    path('nosotros.html', nosotros, name='nosotros'),
    path('index.html', inicio, name='inicio'),
    path('registrarse.html', RegistroUsuario.as_view(), name='registrarse'),
    path('login.html', logeo, name='login'),
    path('loggedId', loggedIn),
    path('logout.html', logout_view, name='logout'),
    path('crear_post.html', crearPost, name='crearpost'),
    path('busqueda.html', Busqueda),
    path('resultado.html', resultado),
    path("contacto.html", contact, name='contacto'),
    path("trabajo.html", trabajo, name='trabajo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("inscripcion.html", inscripcion, name='inscripcion'),
    path('noticias.html', Noticias, name='noticias'),
    path('Detalle/<int:pk>', Detalle_Noticias, name='detalle'),
    path('Comentario/', Comentar_Noticia, name='comentar'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
