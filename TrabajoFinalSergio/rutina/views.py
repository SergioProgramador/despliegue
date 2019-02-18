from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Rutina, Ejercicio, RutinaPersonalizada
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FormularioRutina, RutinaPersonalizadaForm

# Create your views here.
class RutinasListView(ListView):
    model = Rutina

def ejercicios(request, rutina_id):
    rutina = Rutina.objects.get(id=rutina_id)
    return render(request, "rutina/ejercicios.html", {'rutina':rutina})

class RutinaCreateView(CreateView):
    model = Rutina
    template_name = 'rutina/rutina_form.html'
    form_class = FormularioRutina

    def get_success_url(self):
        return reverse_lazy('rutina_list') + '?add'

class RutinaUpdateView(UpdateView):
    model = Rutina
    form_class = FormularioRutina
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('rutina_list') + '?edit'

class RutinaDeleteView(DeleteView):
    model = Rutina

    def get_success_url(self):
        return reverse_lazy('rutina_list') + '?del'


class RutinaPersonalizadaCreateView(CreateView):
    model = RutinaPersonalizada
    template_name = 'rutina/rutina_form_per.html'
    form_class = RutinaPersonalizadaForm

    def get_success_url(self):
        return reverse_lazy('rutina_list') + '?creada'

def RutinaPer_detalle(request):
    rutina=RutinaPersonalizada.objects.all()
    return render(request, 'rutina/rutinap_detalle.html', {'rutina':rutina})

class RutinaPersonalizadaDeleteView(DeleteView):
    model = RutinaPersonalizada
    template_name_suffix = '_confirm2_delete'

    def get_success_url(self):
        return reverse_lazy('rutinap_detalle') + '?del'

class RutinaPersonalizadaUpdateView(UpdateView):
    model = RutinaPersonalizada
    form_class = RutinaPersonalizadaForm
    template_name_suffix = '_update2_form'

    def get_success_url(self):
        return reverse_lazy('rutinap_detalle') + '?edit'