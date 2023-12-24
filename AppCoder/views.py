from datetime import date
from django.shortcuts import redirect, render
from datetime import datetime
from . import models
from .models import Curso, Profesor, Avatar, Mensaje
from .forms import CursoFormulario, CursoBuscarFormulario, ProfesorFormulario, MensajeForm, CursoFormulario
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserCreationFormulario, UserEditionFormulario, UserAvatarFormulario
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.conf import settings
import os
from django.contrib import messages

def inicio_view(request):
    return render(request, "AppCoder/inicio.html")

def cursos_buscar_view(request):
    if request.method == "GET":
        form = CursoBuscarFormulario()
        return render(
            request,
            "AppCoder/curso_formulario_busqueda.html",
            context={"form": form}
        )
    else:
        formulario = CursoBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cursos_filtrados = []
            for titulo in Curso.objects.filter(titulo__icontains=informacion["titulo"]):
                cursos_filtrados.append(titulo)

            contexto = {"titulos": cursos_filtrados}
            return render(request, "AppCoder/cursos_list.html", contexto)

def cursos_todos_view(request):
    todos_los_cursos = []
    for titulo in Curso.objects.all():
        todos_los_cursos.append(titulo)

    contexto = {"titulos": todos_los_cursos}
    return render(request, "AppCoder/cursos_list.html", contexto)


@login_required
def cursos_view(request):
    if request.method == 'POST':
        form = CursoFormulario(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)  # No guardar todavía
            curso.autor = request.user  # Asignar el autor
            curso.save()  # Ahora guardar el objeto Curso

            # Redirige a la vista de lista de cursos, por ejemplo
            return redirect('AppCoder:inicio')
    else:
        form = CursoFormulario()

    # Obtener los cursos creados por el usuario autenticado
    cursos_usuario = Curso.objects.filter(autor=request.user)

    return render(request, "AppCoder/curso_formulario_avanzado.html", {"form": form, "cursos": cursos_usuario})


def profesores_view(xx):
    nombre = "Mariano Manuel"
    apellido = "Barracovich"
    ahora = datetime.now()
    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        "nacionalidad": "argentino",
        "hora": ahora,
        "ciudades_preferidas": ["Buenos Aires", "Lima", "San Pablo", "Trieste"]
    }
    return render(xx, "AppCoder/padre.html", diccionario)

@login_required
def profesor_view(request):
    if request.method == "GET":
        return render(
            request,
            "AppCoder/profesor_formulario_avanzado.html",
            {"form": ProfesorFormulario()}
        )
    else:
        formulario = ProfesorFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Profesor(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
                profesion=informacion["profesion"]
            )
            modelo.save()
        return render(
            request,
            "AppCoder/inicio.html",
        )

@login_required
def profesores_crud_read_view(request):
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/profesores_lista.html", {"profesores": profesores})

@login_required
def profesores_crud_delete_view(request, profesor_email):
    profesor_a_eliminar = Profesor.objects.filter(email=profesor_email).first()
    profesor_a_eliminar.delete()
    return profesores_crud_read_view(request)

@login_required
def profesores_crud_update_view(request, profesor_email):
    profesor = Profesor.objects.filter(email=profesor_email).first()
    if request.method == "GET":
        formulario = ProfesorFormulario(
            initial={
                "nombre": profesor.nombre,
                "apellido": profesor.apellido,
                "email": profesor.email,
                "profesion": profesor.profesion
            }
        )
        return render(request, "AppCoder/profesores_formulario_edicion.html", {"form": formulario, "profesor": profesor})
    else:
        formulario = ProfesorFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            profesor.nombre=informacion["nombre"]
            profesor.apellido=informacion["apellido"]
            profesor.email=informacion["email"]
            profesor.profesion=informacion["profesion"]
            profesor.save()
        return profesores_crud_read_view(request)

class AdminUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class CursoListView(AdminUserMixin, ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "AppCoder/cbv_curso_list.html"

class CursoDetail(AdminUserMixin, DetailView):
    model = Curso
    template_name = "AppCoder/cbv_curso_detail.html"

class CursoCreateView(AdminUserMixin, CreateView):
    model = Curso
    template_name = "AppCoder/cbv_curso_create.html"
    success_url = reverse_lazy("AppCoder:curso-list")
    fields = ["titulo", "subtitulo", "post", "autor", "imagen"]

class CursoDeleteView(AdminUserMixin, DeleteView):
    model = Curso
    template_name = "AppCoder/cbv_curso_delete.html"
    success_url = reverse_lazy("AppCoder:curso-list")

class CursoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Curso
    template_name = "AppCoder/cbv_curso_update.html"
    success_url = reverse_lazy("AppCoder:curso-list")
    fields = ["titulo", "subtitulo", "post", "autor", "imagen"]

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

def login_view(request):
    if request.user.is_authenticated:
        return render(
            request,
            "AppCoder/inicio.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            "AppCoder/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            if modelo is not None:
                login(request, modelo)
                return redirect('AppCoder:mostrar_profile', user_id=modelo.id)
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña es incorrecto")
        
        return render(request, "AppCoder/login.html", {"form": formulario})

def logout_view(request):
    pass


def registro_view(request):
    if request.method == "POST":
        formulario = UserCreationFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            nuevo_usuario = formulario.save()
            imagen_avatar = formulario.cleaned_data.get('imagen')
            
            if imagen_avatar:
                Avatar.objects.create(user=nuevo_usuario, imagen=imagen_avatar)

            return redirect("AppCoder:login")
        else:
            return render(request, "AppCoder/registro.html", {"form": formulario})
    else:
        formulario = UserCreationFormulario()
        return render(request, "AppCoder/registro.html", {"form": formulario})
        
@login_required
def editar_perfil_view(request):
    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).first()

    if request.method == "POST":
        formulario_usuario = UserEditionFormulario(request.POST, instance=usuario)
        formulario_avatar = UserAvatarFormulario(request.POST, request.FILES)

        if formulario_usuario.is_valid() and formulario_avatar.is_valid():
            formulario_usuario.save()

            # Manejo del avatar
            if 'imagen' in request.FILES:
                if avatar:  # Actualizar si ya existe
                    avatar.imagen = request.FILES['imagen']
                    avatar.save()
                else:  # Crear nuevo avatar si no existe
                    nuevo_avatar = Avatar(user=usuario, imagen=request.FILES['imagen'])
                    nuevo_avatar.save()

            return redirect("AppCoder:inicio")

    else:
        valores_iniciales = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }

        formulario_usuario = UserEditionFormulario(initial=valores_iniciales)
        formulario_avatar = UserAvatarFormulario()

    avatar_url = avatar.imagen.url if avatar else ""

    return render(
        request,
        "AppCoder/editar_perfil.html",
        context={
            "formulario_usuario": formulario_usuario,
            "formulario_avatar": formulario_avatar,
            "usuario": usuario,
            "avatar_url": avatar_url
        }
    )

def about_view(request):
    return render(request, "AppCoder/about.html")

def blog_view(request, blog_id):
    blog = get_object_or_404(Curso, pk=blog_id)
    return render(request, 'AppCoder/blog_view.html', {'blog': blog})

def mostrar_profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    todos_los_posts = Curso.objects.filter(autor=user).all()
    avatar = Avatar.objects.filter(user=user).first()
    avatar_url = avatar.imagen.url if avatar is not None else ""
    contexto = {"posts": todos_los_posts, "avatar_url": avatar_url, "user": user}

    return render(request, "AppCoder/profile.html", context=contexto)

@login_required
def enviar_mensaje_view(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('AppCoder:lista_mensajes')
    else:
        form = MensajeForm()
    return render(request, 'enviar_mensaje.html', {'form': form})

@login_required
def lista_mensajes_view(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'lista_mensajes.html', {'mensajes': mensajes_recibidos})

