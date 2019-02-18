from .models import Actividad, Instructor
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import FormularioActividad

# Create your views here.
class ActividadListView(ListView):
    model = Actividad

class ActividadDetailView(DetailView):
    model = Actividad

class ActividadCreate(CreateView):
    model = Actividad
    template_name = 'actividad/actividad_form.html'
    form_class = FormularioActividad

    def get_success_url(self):
        return reverse_lazy('actividad_list') + '?add'

class ActividadUpdateView(UpdateView):
    model = Actividad
    form_class = FormularioActividad
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('actividad_list') + '?edit'

class ActividadDeleteView(DeleteView):
    model = Actividad

    def get_success_url(self):
        return reverse_lazy('actividad_list') + '?del'

