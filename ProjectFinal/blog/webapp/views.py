from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import PostForm
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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

# def registrarse(request):
#     return render(request, 'registrarse.html')
class RegistroUsuario(CreateView):
    model = User
    template_name = 'registrarse.html'
    form_class = ResgistroForm
    success_url = reverse_lazy('login')

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin

    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect) # Este decorador agrega protección CSRF
    @method_decorator(never_cache)
    def dispatch(self, request, *args , **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else: 
            return super(Login,self).dispatch(request, *args, **kwargs)

    def form_valid(self, form) :
        login(self.request,form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')


# def login(request):
#     return render(request, 'login.html')
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