from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy 
from django import forms
from django.shortcuts import render

# Create your views here.
class Register(CreateView):
    form_class = UserCreationFormWithEmail
    succes_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(Register, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb3', 'placeholder':'Nombre de usuario', 'style':'width: 10cm'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb3', 'placeholder':'Email', 'style':'width: 10cm'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb3', 'placeholder':'Contraseña', 'style':'width: 10cm'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb2', 'placeholder':'Repita la contraseña', 'style':'width: 10cm'})
        return form

# def LoginFacebook(request, *args, **kwargs):
#     return render(request, 'auth/login.html')