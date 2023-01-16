from django.urls import path

from estudiantes.views import (
    listar_estudiantes, listar_profesores, listar_cursos,
    crear_curso, buscar_cursos, ver_curso, editar_curso
)


urlpatterns = [
    path('alumnos/', listar_estudiantes, name="listar_alumnos"),
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('crear-curso/', crear_curso, name="crear_curso"),
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
    path('cursos/<int:id>/', ver_curso, name="ver_curso"),
    path('editar-curso/<int:id>/', editar_curso, name="editar_curso"),
]
