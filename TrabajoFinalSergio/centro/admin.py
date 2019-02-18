from django.contrib import admin
from .models import Centro

# Register your models here.

class CentroAdmin(admin.ModelAdmin): # Clase para solo leer los campos de creacion y actualizacion en el panel de administracion
    readonly_fields = ('created' , 'updated')

admin.site.register(Centro, CentroAdmin)

