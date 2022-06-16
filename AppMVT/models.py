from django.db import models

# Create your models here.


class Familiar(models.Model):
    nombre = models.CharField(max_length = 30) # tipo de dato caracteres has 40 caracteres (string)
    #apellido = models.CharField(max_length = 30) # en los campos CharField hay que detallar el max_length si no tira error
    email = models.EmailField() # tipo de dato email
    #profesion = models.CharField(max_length = 30)
    fechaDeNacimiento = models.DateField() #tipo de dato fecha
    tieneEmpleo = models.BooleanField() # tipo de dato booleano

class Amigos(models.Model):
    nombre = models.CharField(max_length = 30) 
    #apellido = models.CharField(max_length = 30) 
    email = models.EmailField() 
    #profesion = models.CharField(max_length = 30)
    fechaDeNacimiento = models.DateField() 
    tieneEmpleo = models.BooleanField() 


    #para modificar una class como en este ejemplo que retiramos 2 atributos se deben volver a correr los comandos:
    # python manage.py makemigrations
    # python manage.py migrate