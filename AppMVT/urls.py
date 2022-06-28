from django.urls import path

from AppMVT import views

urlpatterns = [
   
    path('inicio', views.inicio), 
    path('familiares', views.agragarFamiliar, name='familiares'), 
    path('amigos', views.agragarAmigo, name='amigos'), 
    path('autos', views.Auto, name='autos'), 

    path('buscarAuto', views.buscarAuto, name='buscarAuto'),  


]