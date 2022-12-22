from django.http import HttpResponse
from .models import *
from .forms import PostForm, LoginForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from mysqlx import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from functools import wraps
from django.urls import reverse_lazy
from .forms import *


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

def Noticias(request):
    n = Noticia.objects.all()
    contexto = {'noticias': n}
    return render(request, 'noticias.html', contexto)

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
                    message = "No logeado"
            else:
                message = "Nombre de usuario y/o contraseña incorrecta"
    else:
        form = LoginForm
    return render(request, 'login.html', {'message': message, 'form': form})


def trabajo(request):
    return render(request, 'trabajo.html')

@login_required
def crearPost(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('crear_post.html')
    else:
        post_form = PostForm()
    return render(request, 'crear_post.html', {'post_form': post_form})

@login_required
def Busqueda(request):
    if request.GET["post"]:
        # mensaje = "Buscar: %r" %request.GET["post"]
        elemento_buscado = request.GET["post"]
        articulo = Categoria.objects.filter(nombre__icontains=elemento_buscado)
        return render(request, "resultado.html", {"articulo": articulo, "query": elemento_buscado})

    else:
        mensaje = "busqueda vacía"
    return HttpResponse(mensaje)


def resultado(request):
    return render(request, 'resultado.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Consulta de la Pagina Web Bomberos Voluntarios"
            body = {
                'Nombre': form.cleaned_data['Nombre'],
                'Apellido': form.cleaned_data['Apellido'],
                'Correo Electronico': form.cleaned_data['Correo_Electronico'],
                'Mensaje': form.cleaned_data['Mensaje'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'correoelectronico@gmail', ['correelectronic@gmail.com']) and messages.success(
                    request, "Formulario Enviado, Gracias por contactarse con nosotros")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/contacto.html")

    form = ContactForm()
    return render(request, "contacto.html", {'form': form})


def loggedIn(request):
    if request.user.is_authenticated:
        respuesta = 'Estas loge-ado como: ' + request.user.username
    else:
        respuesta = "No estas logueado. <a href='login.html'>Logeate</a>"
    return HttpResponse(respuesta)


def logout_view(request):
    logout(request)
    return redirect('index.html')

def inscripcion(request):
    return render(request, 'inscripcion.html')
    

def Listar_Noticias(request):
    contexto = {}

    id_categoria = request.GET.get('id',None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria)
    else:
        n = Noticia.objects.all() #RETORNA UNA LISTA DE OBJETOS

    contexto['noticias'] = n

    cat = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = cat

    return render(request, 'noticias/listar.html', contexto) 

@login_required
def Comentar_Noticia(request):

    com = request.POST.get('comentario',None)
    usu = request.user
    noti = request.POST.get('id_post', None)
    post = Noticia.objects.get(id = noti) 
    Comentario.objects.create(usuario = usu, posteo = post, texto = com)

    return redirect(reverse_lazy('detalle', kwargs={'pk': noti}))   


def Detalle_Noticias(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO
    contexto['noticia'] = n

    c = Comentario.objects.filter(noticia = n)
    contexto['comentarios'] = c

    return render(request, 'detalle.html',contexto)
