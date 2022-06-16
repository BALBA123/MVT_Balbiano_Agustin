from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context, loader
from AppMVT.models import Familiar, Amigos


# Create your views here.


def inicio(request):
    return render(request, "nuestro_primer_MVT/inicio.html") 


def familiares(request):
    return render(request, "nuestro_primer_MVT/familiares.html") 

def familiar(self):

    familiar1 = Familiar(nombre="veronica", email="veroB@gmail.com", fechaDeNacimiento="2001-02-15", tieneEmpleo=True)
    familiar1.save()

    familiar2 = Familiar(nombre="gustavo", email="gustavo@gmail.com", fechaDeNacimiento="1996-09-18", tieneEmpleo=True)
    familiar2.save()

    familiar3 = Familiar(nombre="carlos", email="carlos@gmail.com", fechaDeNacimiento="1901-12-15", tieneEmpleo=False)
    familiar3.save()    

    Documento = f"Familiar1<br>nombre: {familiar1.nombre} <br>email: {familiar1.email} <br>fecha de nacimiento: {familiar1.fechaDeNacimiento} <br>tiene empleo: {familiar1.tieneEmpleo}<br><br>Familiar2<br>nombre: {familiar2.nombre} <br>email: {familiar2.email} <br>fecha de nacimiento: {familiar2.fechaDeNacimiento} <br>tiene empleo: {familiar2.tieneEmpleo}<br><br>Familiar3<br>nombre: {familiar3.nombre} <br>email: {familiar3.email} <br>fecha de nacimiento: {familiar3.fechaDeNacimiento} <br>tiene empleo: {familiar3.tieneEmpleo}<br><br>"

    return HttpResponse(Documento)




def amigos(request):
    return render(request, "nuestro_primer_MVT/amigos.html") 


def amigo(self):

    amigo1 = Amigos(nombre="veronica", email="veroB@gmail.com", fechaDeNacimiento="2001-02-15", tieneEmpleo=True)
    amigo1.save()
    texto = f"Amigo1<br>nombre: {amigo1.nombre} <br>email: {amigo1.email} <br>fecha de nacimiento: {amigo1.fechaDeNacimiento} <br>tiene empleo: {amigo1.tieneEmpleo}"
    
    plantilla = loader.get_template("nuestro_primer_MVT/amigos.html")

    Documento = plantilla.render(texto)

    return HttpResponse(Documento)