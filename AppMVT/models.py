from django.db import models

# Create your models here.


class familiar(models.Model):
    nombre = models.CharField(max_length = 30) # tipo de dato caracteres has 40 caracteres (string)
    apellido = models.CharField(max_length = 30) # en los campos CharField hay que detallar el max_length si no tira error
    email = models.EmailField() # tipo de dato email
    profesion = models.CharField(max_length = 30)
    fechaDeNacimiento = models.DateField() #tipo de dato fecha
    tieneEmpleo = models.BooleanField() # tipo de dato booleano

class amigos(models.Model):
    nombre = models.CharField(max_length = 30) 
    apellido = models.CharField(max_length = 30) 
    email = models.EmailField() 
    profesion = models.CharField(max_length = 30)
    fechaDeNacimiento = models.DateField() 
    tieneEmpleo = models.BooleanField() 