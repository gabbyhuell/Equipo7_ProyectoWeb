from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import PostForm
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages

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

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Consulta de la Pagina Web Bomberos Voluntarios" 
			body = {
			'Nombre': form.cleaned_data['Nombre'], 
			'Apellido': form.cleaned_data['Apellido'], 
			'Correo Electronico': form.cleaned_data['Correo_Electronico'], 
			'Mensaje':form.cleaned_data['Mensaje'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'enzi132011@hotmail.com', ['enzo_hca@hotmail.com']) and messages.success(request, "Formulario Enviado, Gracias por contactarse con nostros") 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/contacto.html")

	form = ContactForm()
	return render(request, "contacto.html", {'form':form})


        