from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from estudiantes.models import Estudiante, Profesor, Curso


def inicio(request):
    return render(
        request=request,
        template_name='estudiantes/inicio.html',
    )


def listar_estudiantes(request):
    ## Aqui iria la validacion del permiso lectura estudiantes
    contexto = {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_estudiantes.html',
        context=contexto,
    )


def listar_profesores(request):
    contexto = {
        'profesores': Profesor.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_profesores.html',
        context=contexto,
    )


def listar_cursos(request):
    contexto = {
        'cursos': Curso.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_cursos.html',
        context=contexto,
    )


def crear_curso(request):
    if request.method == "POST":
        data = request.POST
        curso = Curso(nombre=data['nombre'], comision=data['comision'])
        curso.save()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)
    else:  # GET
        return render(
            request=request,
            template_name='estudiantes/formulario_curso.html',
        )
