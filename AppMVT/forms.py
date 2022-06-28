from django import forms



class formularioFamiliar(forms.Form):
    nombre = forms.CharField(max_length = 30) 
    email = forms.EmailField() 


class formularioAmigos(forms.Form):
    nombre = forms.CharField(max_length = 30) 
    email = forms.EmailField() 
    fechaDeNacimiento = forms.DateField()