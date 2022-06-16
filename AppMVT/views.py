from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from AppMVT.models import Familiar, Amigos


# Create your views here.


def inicio(request):
    return render(request, "nuestro_primer_MVT/inicio.html") 


def familiares(request):
    return render(request, "nuestro_primer_MVT/familiares.html") 

def familiar(self):

    familiar1 = Familiar(nombre="veronica", email="veroB@gmail.com", fechaDeNacimiento="2001-02-15", tieneEmpleo=True)
    familiar1.save()
    Documento = f"Amigo1<br>nombre: {familiar1.nombre} <br>email: {familiar1.email} <br>fecha de nacimiento: {familiar1.fechaDeNacimiento} <br>tiene empleo: {familiar1.tieneEmpleo}"

    return HttpResponse(Documento)






def amigos(request):
    return render(request, "nuestro_primer_MVT/amigos.html") 


def amigo(self):

    amigo1 = Amigos(nombre="veronica", email="veroB@gmail.com", fechaDeNacimiento="2001-02-15", tieneEmpleo=True)
    amigo1.save()
    Documento = f"Amigo1<br>nombre: {amigo1.nombre} <br>email: {amigo1.email} <br>fecha de nacimiento: {amigo1.fechaDeNacimiento} <br>tiene empleo: {amigo1.tieneEmpleo}"

    return HttpResponse(Documento)