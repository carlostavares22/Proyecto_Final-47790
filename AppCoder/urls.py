from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.conf.urls import handler404, handler403
from django.conf import settings
from AppCoder.views import (
    cursos_view,
    cursos_buscar_view,
    cursos_todos_view,
    inicio_view,
    profesores_view,
    ### CRUD
    profesores_crud_delete_view,
    profesores_crud_read_view,
    profesores_crud_update_view,
    profesor_view,
    CursoCreateView,
    CursoDetail,
    CursoDeleteView,
    CursoListView,
    CursoUpdateView,
    ### LOGIN
    login_view,
    registro_view,
    editar_perfil_view,
    about_view,
    blog_view,
    mostrar_profile_view,
    )


app_name = "AppCoder"

if settings.DEBUG:
    from django.views.defaults import page_not_found, permission_denied

urlpatterns = [
    path("pages/", cursos_view, name="cursos"),
    path("cursos/todos", cursos_todos_view, name="cursos-todos"),
    path("pages/search", cursos_buscar_view, name="cursos-buscar"),
    path("comisiones/", profesores_view),
    path("inicio/", inicio_view, name="inicio"),
    ###### CRUD
    path("profesores/", profesor_view),
    path("profesores-lista/", profesores_crud_read_view),
    path("profesores-eliminar/<profesor_email>/", profesores_crud_delete_view),
    path("profesores-editar/<profesor_email>/", profesores_crud_update_view),
    ###### CBV
    path("curso/list", CursoListView.as_view(), name="curso-list"),
    path("curso/new", CursoCreateView.as_view(), name="curso-create"),
    path("curso/<pk>", CursoDetail.as_view(), name="curso-detail"),
    path("curso/<pk>/update", CursoUpdateView.as_view(), name="curso-update"),
    path("curso/<pk>/delete", CursoDeleteView.as_view(), name="curso-delete"),
    ###### LOGIN
    path("registro", registro_view, name="registro"),
    path("login", login_view, name="login"),
    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    #### EDIT USER
    path("editar-perfil", editar_perfil_view, name="editar-perfil"),
    #### ABOUT
    path("about", about_view, name="about"),
    # AppCoder/urls.py
    path('blog/<int:blog_id>/', views.blog_view, name='blog_view'),
    path('profile/<int:user_id>/', views.mostrar_profile_view, name='mostrar_profile'),
    path('enviar_mensaje/', views.enviar_mensaje_view, name='enviar_mensaje'),
    path('mensajes/', views.lista_mensajes_view, name='lista_mensajes'),
    path('404/', page_not_found, kwargs={'exception': Exception('Página no encontrada')}),
    path('403/', permission_denied, kwargs={'exception': Exception('Acceso denegado')}),
]
