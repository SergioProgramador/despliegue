from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.core.mail import EmailMessage
from .forms import FormularioContacto

# Create your views here.
def send_email(request):
    if request.method == 'POST':
        formulario=FormularioContacto(request.POST)
        if formulario.is_valid():
            nombre=formulario.cleaned_data['nombre']
            apellido=formulario.cleaned_data['apellido']
            asunto='Mensaje de '+nombre+' '+apellido+'. Valoración sobre la página web.'
            mensaje=formulario.cleaned_data['mensaje']
            mail=EmailMessage(asunto, mensaje, to=['felixreyesf@gmail.com'])
            mail.send()
        return render(request, 'contacto/gracias.html')
    else:
        formulario = FormularioContacto()
    return render(request, 'contacto/contactar.html', {'formulario' : formulario})