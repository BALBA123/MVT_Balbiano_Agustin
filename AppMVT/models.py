from django.db import models

# Create your models here.


class Familiar(models.Model):
    nombre = models.CharField(max_length = 30) # tipo de dato caracteres has 40 caracteres (string)
    
    email = models.EmailField() # tipo de dato email
    
    
    

class Amigos(models.Model):
    nombre = models.CharField(max_length = 30) 
 
    email = models.EmailField() 

    fechaDeNacimiento = models.CharField(max_length = 10) 
     

class auto(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    numeroPatente= models.IntegerField()


    #para modificar una class como en este ejemplo que retiramos 2 atributos se deben volver a correr los comandos:
    # python manage.py makemigrations
    # python manage.py migrate