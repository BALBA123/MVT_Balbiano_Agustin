from django.urls import path

from AppMVT import views

urlpatterns = [
   
    path('', views.inicio), 
    path('familiares', views.familiares),
    path('amigos', views.amigos),

]