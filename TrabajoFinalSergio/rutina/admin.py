from django.contrib import admin
from .models import Rutina, Ejercicio, RutinaPersonalizada

# Register your models here.
class RutinaAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'updated')

class EjercicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'updated')

class RutinaPersonalizadaAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'updated')

admin.site.register(Rutina, RutinaAdmin)
admin.site.register(Ejercicio, EjercicioAdmin)
admin.site.register(RutinaPersonalizada, RutinaPersonalizadaAdmin)



