from django.shortcuts import render
from .models import Centro
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FormularioCentro
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    centros = Centro.objects.all() # nos devuelve todos los objetos que tiene el modelo
    return render(request, "centro/home.html", {'centros': centros})

class CentroCreateView(CreateView):
    model = Centro
    template_name = 'centro/centro_form.html'
    form_class = FormularioCentro

    def get_success_url(self):
        return reverse_lazy('home') + '?add'
    
class CentroUpdateView(UpdateView):
    model = Centro
    form_class = FormularioCentro
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('home') + '?edit'

class CentroDeleteView(DeleteView):
    model = Centro

    def get_success_url(self):
        return reverse_lazy('home') + '?del'
