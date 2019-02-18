from django import forms
from .models import Rutina, Ejercicio, RutinaPersonalizada

class FormularioRutina(forms.ModelForm):

    class Meta:
        model = Rutina
        fields = ('titulo', 'descripcion', 'imagen', 'ejercicios')
        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control', 'style':'width:10cm'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control', 'style':'width:10cm', 'rows':'5'}),
            'ejercicios' : forms.SelectMultiple(attrs={'class':'form-control', 'style':'width:10cm'}),

        }
        labels = {
            'titulo' : 'TÍTULO',
            'descripcion' : 'DESCRIPCIÓN',
            'imagen' : 'IMAGEN',
            'ejercicios' : 'EJERCICICOS',
        }

class RutinaPersonalizadaForm(forms.ModelForm):
    
    class Meta:
        model = RutinaPersonalizada
        fields = ('titulo', 'descripcion', 'imagen', 'ejercicios')
        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control', 'style':'width:10cm'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control', 'style':'width:10cm', 'rows':'5'}),
            'ejercicios' : forms.SelectMultiple(attrs={'class':'form-control', 'style':'width:10cm'}),

        }
        labels = {
            'titulo' : 'TÍTULO',
            'descripcion' : 'DESCRIPCIÓN',
            'imagen' : 'IMAGEN',
            'ejercicios' : 'EJERCICICOS',
        }