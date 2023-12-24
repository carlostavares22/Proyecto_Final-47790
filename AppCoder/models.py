from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

def get_default_user():
    user, created = User.objects.get_or_create(username='Anónimo')
    return user.id  # Asegúrate de devolver el ID, no el objeto User

class Curso(models.Model):
    titulo = models.CharField(max_length=100, default="Título por defecto")  # Título del blog post
    subtitulo = models.CharField(max_length=100, default="Subtítulo por defecto")
    post = models.TextField(null=True, blank=True)  # Contenido del post
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    imagen = models.FileField(upload_to="media/post", null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.post})"
    
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
    

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name='mensajes_remitidos', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField(max_length=50)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensaje de {self.remitente} a {self.destinatario}"
