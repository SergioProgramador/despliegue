from django.contrib import admin
from .models import Inscripcion

# Register your models here.

class InscripcionAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'updated')

admin.site.register(Inscripcion, InscripcionAdmin)
    
