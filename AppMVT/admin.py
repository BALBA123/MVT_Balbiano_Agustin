from django.contrib import admin
from .models import * #importamos el archivo models
# Register your models here.

#superusuario:
    #usuario = agustin
    #contraseña = 123

admin.site.register(Familiar)

admin.site.register(Amigos)

admin.site.register(auto)

