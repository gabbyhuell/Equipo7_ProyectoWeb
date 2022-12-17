from django.contrib import admin
from .models import *
# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo','teaser', 'contenido', 'imagen', 'categoria', 'usuario')

admin.site.register(Direccion)
admin.site.register(Categoria)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Usuario)
admin.site.register(Web)
admin.site.register(RedesSociales)
admin.site.register(Contacto)
admin.site.register(Comentario)
