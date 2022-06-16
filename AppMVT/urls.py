from django.urls import path

from AppMVT import views

urlpatterns = [
   
    path('', views.inicio), 
    path('familiares', views.familiar),
    path('amigos', views.amigo),

    path('familiaresss', views.familiares),

]