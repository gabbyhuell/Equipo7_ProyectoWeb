from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from mysqlx import View

from .models import *
from .forms import PostForm, LoginForm
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from functools import wraps

# Create your views here.
def bienvenido(request):
    mensajes = {
        'mensaje1': 'Block equipo 7',
        'mensaje2': 'Estación de Bomberos'
    }
    return render(request, 'bienvenido.html', mensajes)

def despedirse(request):
    return HttpResponse("despedida desde Django")

def nosotros(request):
    return render(request, 'nosotros.html')

def inicio(request):
    return render(request, 'index.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def logeo(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Logueado"
                    return redirect('index.html')
                else:
                    message = "No legeado"
            else:
                message = "Nombre de usuario y/o contraseña incorrecta"
    else:
        form = LoginForm
    return render(request, 'login.html', {'message': message, 'form': form})

def crearPost(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('crear_post.html')
    else:
        post_form = PostForm()
    return render(request, 'crear_post.html', {'post_form': post_form})


def Busqueda(request):
    if request.GET["post"]:
        #mensaje = "Buscar: %r" %request.GET["post"]
        elemento_buscado = request.GET["post"]
        articulo = Categoria.objects.filter(nombre__icontains = elemento_buscado)
        return render(request,"resultado.html",{"articulo":articulo, "query":elemento_buscado})

    else:
        mensaje = "busqueda vacia"
    return HttpResponse(mensaje)

def resultado(request):
    return render(request, 'resultado.html')

def loggedIn(request):
    if request.user.is_authenticated:
        respuesta = 'Estas logeado como: ' + request.user.username
    else:
        respuesta = "No estas logueado. <a href='login.html'>Logeate</a>"
    return HttpResponse(respuesta)


def logout_view(request):
    logout(request)
    return redirect('index.html')


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(LoginRequiredMixin, View):
    template_name = 'home.html'