from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Direccion(models.Model):
    calle = models.CharField(max_length=255)
    no_casa = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255, null=True, blank=True)
    provincia = models.CharField(max_length=255, null=True, blank=True)
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_casa} {self.localidad}'


class Categoria(models.Model):
    nombre = models.CharField('Nombre de la categoria', max_length=100, unique=True)

    class Metta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorie'

    def __str__(self):
        return self.nombre



class Usuario(models.Model):
    nombre = models.CharField('Nombres', max_length=50)
    apellido = models.CharField('Apellidos', max_length=50)
    usuario = models.CharField('Usario registrado', max_length=50)
    email = models.EmailField('Correo electronico', max_length=255)
    passw = models.CharField(max_length=60)
    passwConfirmacion = models.CharField(max_length=60)
    estatus = models.BooleanField('Activo / Inactivo', default=False)
    tipo = models.IntegerField('Admin / visitante', default=0)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False,
                                      auto_now_add=True)  # auto_now_add fecha autom. en el momento de creacion
    fecha_actualizacion = models.DateField('Fecha de modificacion', auto_now=True,
                                           auto_now_add=False)  # auto_now fecha automaticamente cada vez que el registro se modifique
    fecha_eliminacion = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False)
    imagen = models.ImageField('Imagen', upload_to='categoria/', max_length=255)

    class Metta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'Usuario {self.id}: {self.nombre} {self.apellido} {self.email}'



class Noticia(models.Model):
    titulo = models.CharField('Titulo', max_length=255)
    teaser = models.CharField('Resumen', max_length=511)
    contenido = RichTextField()
    imagen = models.ImageField('Imagen', upload_to='categoria/', max_length=255)
    estatus = models.BooleanField('Publicado / No publicado', default=False)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False,
                                      auto_now_add=True, null=True, blank=True)  # auto_now_add fecha autom. en el momento de creacion
    fecha_actualizacion = models.DateField('Fecha de modificacion', auto_now=True,
                                           auto_now_add=False, null=True, blank=True)  # auto_now fecha automaticamente cada vez que el registro se modifique
    fecha_eliminacion = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False,  null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)


    class Metta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return f'Usuario {self.id}: {self.nombre} {self.apellido} {self.email}'




class Web(models.Model):
        nosotros = models.TextField('Nosotros')
        telefono = models.CharField('Telefono', max_length=13)
        email = models.EmailField('Correo Electronico', max_length=255)
        direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)

        class Metta:
            verbose_name = 'Web'
            verbose_name_plural = 'Webs'

        def __str__(self):
            return f'Nosotros'

class RedesSociales(models.Model):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('twitter')
    instagram = models.URLField('instagram')

    class Metta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.facebook

class Contacto(models.Model):
    nombre = models.CharField('Nombres', max_length=50)
    apellido = models.CharField('Apellidos', max_length=50)
    email = models.EmailField('Correo electronico', max_length=255)
    asunto = models.CharField('Motivo de Contacto', max_length=100)
    mensaje = models.TextField('Mensaje')

    class Metta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.asunto


class Comentario(models.Model):
    comentario = models.CharField('Nombres', max_length=255)
    estatus = models.BooleanField('Publicado / No publicado', default=False)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False,
                                      auto_now_add=True, null=True,
                                      blank=True)  # auto_now_add fecha autom. en el momento de creacion
    fecha_actualizacion = models.DateField('Fecha de modificacion', auto_now=True,
                                           auto_now_add=False, null=True,
                                           blank=True)  # auto_now fecha automaticamente cada vez que el registro se modifique
    fecha_eliminacion = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False, null=True,
                                         blank=True)
    noticia = models.ForeignKey(Noticia, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    class Metta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.asunto
