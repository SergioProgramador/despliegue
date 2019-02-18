from django import forms
from .models import Inscripcion
from captcha.fields import ReCaptchaField

class FormularioInscripcion(forms.ModelForm):

    captcha = ReCaptchaField()

    def save(self, commit=True, *args, **kwargs):
        request = None
        if  kwargs is not None and 'request' in kwargs:
            request = kwargs.pop('request')
        r = super().save(commit=False, *args, **kwargs)  
        if 'user' not in kwargs and request is not None:
            r.user = request.user
            r.save()

    class Meta:
        model = Inscripcion
        exclude = ['user', 'cuota']
        # fields = ('nombre', 'apellidos', 'dni', 'edad', 'telefono', 'ciudad', 'cuenta_bancaria', 'cuota')
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'style':'width:8cm'}),
            'apellidos' : forms.TextInput(attrs={'class':'form-control', 'style':'width:8cm'}),
            'dni' : forms.TextInput(attrs={'class':'form-control', 'style':'width:8cm'}),
            'edad' : forms.NumberInput(attrs={'class':'form-control', 'style':'width:8cm'}),
            'telefono' : forms.NumberInput(attrs={'class':'form-control', 'style':'width:8cm'}),
            'ciudad' : forms.TextInput(attrs={'class':'form-control', 'style':'width:8cm'}),
            'cuenta_bancaria' : forms.TextInput(attrs={'class':'form-control', 'style':'width:8cm'}),
        }
        labels = {
            'nombre' : 'NOMBRE',
            'apellidos' : 'APELLIDOS',
            'dni' : 'DNI',
            'edad' : 'EDAD',
            'telefono' :'TELEFONO',
            'ciudad' : 'CIUDAD',
            'cuenta_bancaria' : 'CUENTA BANCARIA',
 
        }
    
    #Hago la cuenta bancaria única
    def clean_cuenta_bancaria(self): 
        cuenta_bancaria = self.cleaned_data.get("cuenta_bancaria")
        if Inscripcion.objects.filter(cuenta_bancaria=cuenta_bancaria).exists():
            raise forms.ValidationError("La cuenta bancaria ya ha sido registrada.")
        return cuenta_bancaria

    def clean_user(self, request): 
        self.user = request.user
        if Inscripcion.objects.filter(user_id=self.user).exists():
            raise forms.ValidationError("Ya te has inscrito en este gimnasio.")
        return self.user
