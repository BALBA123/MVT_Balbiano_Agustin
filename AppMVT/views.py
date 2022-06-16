#from xml.dom.minidom import Document
from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.


def inicio(request):
    return render(request, "nuestro_primer_MVT/inicio.html") 

def familiares(request):
    return render(request, "nuestro_primer_MVT/familiares.html") 

def amigos(request):
    return render(request, "nuestro_primer_MVT/amigos.html") 