from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import PostForm
from django.shortcuts import render, redirect

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

def login(request):
    return render(request, 'login.html')

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