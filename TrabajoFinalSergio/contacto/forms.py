from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    telefono = forms.IntegerField()
    mensaje = forms.CharField(max_length=500)
    

