from django.contrib import admin
from .models import Instructor, Actividad

# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'updated')

class ActividadAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'updated')

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Actividad, ActividadAdmin)
