from django.shortcuts import render, HttpResponseRedirect
from .models import Inscripcion
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView 
from django.urls import reverse_lazy
from .forms import FormularioInscripcion

# Create your views here.

class InscripcionHomeView(TemplateView):
    template_name = 'inscripcion/inscripcion_home.html'


class InscripcionCreate(CreateView):
    model = Inscripcion
    template_name = 'inscripcion/inscripcion_form.html'
    form_class = FormularioInscripcion

    def get_success_url(self):
        return reverse_lazy('inscripcion_home') + '?ins'

    def form_valid(self, form):
        self.object = form.save(request=self.request)
        return HttpResponseRedirect(self.get_success_url())
        

def Inscripcion_detalle(request):
    if(Inscripcion.objects.filter(user=request.user).exists()):
        inscripcion=Inscripcion.objects.get(user=request.user)
        return render(request, 'inscripcion/inscripcion_detalle.html', {'inscripcion':inscripcion})
    else:
        nop=True
        return render(request, 'inscripcion/inscripcion_home.html', {'nop':nop})

class InscripcionUpdate(UpdateView):
    model = Inscripcion
    form_class = FormularioInscripcion
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('inscripcion_detalle') + '?edit'

class InscripcionDelete(DeleteView):
    model = Inscripcion

    def get_success_url(self):
        return reverse_lazy('inscripcion_home') + '?del'





    





   
       
        
		