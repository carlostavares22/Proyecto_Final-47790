from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel
from .models import Avatar
from .models import Curso
from django.contrib.auth import get_user_model
from .models import Mensaje

UserModel = get_user_model()

class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    imagen = forms.ImageField(label='Imagen de perfil', required=False)

    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", "imagen"]
        help_texts = {k: "" for k in fields}


class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'subtitulo', 'post', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'titulo': 'Título',
            'subtitulo': 'Subtítulo',
            'post': 'Contenido',
            'imagen': 'Imagen',
        }

class CursoBuscarFormulario(forms.Form):
    titulo = forms.CharField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()


class UserEditionFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}

class UserAvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ["imagen"]

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']
