from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    mensajes = {
        'mensaje1': 'Block equipo 7',
        'mensaje2': 'Estación de Bomberos'
    }
    return render(request, 'bienvenido.html', mensajes)

def despedirse(request):
    return HttpResponse("despedida desde Django")