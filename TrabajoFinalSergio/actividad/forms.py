from django import forms
from .models import Actividad

class FormularioActividad(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ('nombre', 'descripcion', 'duracion', 'tipo_ejercicio', 'caloria', 'beneficio', 'imagen', 'instructor')
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'style':'width:10cm'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control', 'style':'width:10cm', 'rows':'5'}),
            'duracion' : forms.NumberInput(attrs={'class':'form-control', 'style':'width:10cm'}),
            'tipo_ejercicio' : forms.TextInput(attrs={'class':'form-control', 'style':'width:10cm'}),
            'caloria' : forms.NumberInput(attrs={'class':'form-control', 'style':'width:10cm', 'rows':'5'}),
            'beneficio' : forms.TextInput(attrs={'class':'form-control', 'style':'width:10cm'}),
            'instructor' : forms.Select(attrs={'class':'form-control', 'style':'width:10cm'}),
        }
        labels = {
            'nombre' : 'NOMBRE',
            'descripcion' : 'DESCRIPCIÓN',
            'duracion' : 'DURACIÓN',
            'tipo_ejercicio' : 'TIPO DE EJERCICIO',
            'caloria' : 'CALORÍAS',
            'beneficio' : 'BENEFICIO',
            'imagen' : 'IMAGEN',
            'instructor' : 'INSTRUCTOR',
        }