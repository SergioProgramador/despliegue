from django import forms
from .models import Centro

class FormularioCentro(forms.ModelForm):

    class Meta:
        model = Centro
        fields = ('nombre', 'direccion', 'email', 'ciudad', 'horario', 'imagen')
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'style':'width:8cm'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control', 'style':'width:8cm'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'style':'width:8cm'}),
            'ciudad' : forms.TextInput(attrs={'class':'form-control', 'style':'width:8cm'}),
            'horario' : forms.Textarea(attrs={'class':'form-control', 'style':'width:8cm', 'rows':'4'}),
        }
        labels = {
            'nombre' : 'NOMBRE',
            'direccion' : 'DIRECCIÓN',
            'email' : 'EMAIL',
            'ciudad' : 'CIUDAD',
            'telefono' :'TELEFONO',
            'horario' : 'HORARIO',
            'imagen' : 'IMAGEN',
 
        }