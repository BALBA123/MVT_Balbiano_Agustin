

from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context, loader
from AppMVT.models import Familiar, Amigos, auto
from AppMVT.forms import formularioFamiliar, formularioAmigos


# Create your views here.


def inicio(request):
    return render(request, "AppMVT/inicio.html") 

def agragarFamiliar(request):

    if request.method == "POST":

        miFormulario = formularioFamiliar(request.POST) # aca llega toda la info del HTML

        print(miFormulario)

        if miFormulario.is_valid: #validacion de django
            
            info = miFormulario.cleaned_data #

            familiar = Familiar (nombre=info['nombre'], email=info['email'])
            
            familiar.save()

            return render(request, "AppMVT/inicio.html")
    else:

        miFormulario = formularioFamiliar() #formulario vacio para construir el HTML
        return render(request, "AppMVT/familiares.html", {"miFormulario":miFormulario})


def agragarAmigo(request):

    if request.method == "POST":

        miFormulario = formularioAmigos(request.POST) # aca llega toda la info del HTML

        print(miFormulario)

        if miFormulario.is_valid: #validacion de django
            
            info = miFormulario.cleaned_data #
            print(info)
            Amigo = Amigos (nombre=info['nombre'], email=info['email'], fechaDeNacimiento=info['fechaDeNacimiento'])
            
            Amigo.save()

            return render(request, "AppMVT/inicio.html")
    else:

        miFormulario = formularioAmigos() #formulario vacio para construir el HTML
        return render(request, "AppMVT/amigos.html", {"miFormulario":miFormulario})


def Auto(request):

    return render(request, "AppMVT/auto.html")

def buscarAuto(request):

    if request.GET['patente']:

        patente =request.GET['patente'] # aca solo renvio lo que piden
        print(patente)
        numero = auto.objects.filter(numeroPatente__icontains=patente) # verificar si el orden dentro de los parentesis es correcto
        print(numero)
        modelo = auto.objects.filter(numeroPatente__icontains=patente)
# 
        return render(request, "AppMVT/auto.html", {"marca":numero, "modelo":modelo, "numeroPatente":patente })

    else:
        respuesta = "no ingresaste numero de patente"

    return render(request, "AppMVT/auto.html")


