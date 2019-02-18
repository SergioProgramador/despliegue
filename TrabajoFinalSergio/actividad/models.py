from django.db import models

# Create your models here.
class Instructor(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    apellidos = models.CharField(max_length=250, verbose_name="Apellidos")
    dni = models.CharField(max_length=100, verbose_name="DNI")
    edad = models.IntegerField(verbose_name="Edad")
    sexo = models.CharField(max_length=50, verbose_name="Sexo")
    especialidad = models.CharField(max_length=300, verbose_name="Especialidad")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="instructores")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="instructor"
        verbose_name_plural="instructores"
        ordering=["created"]

    def __str__(self): #Este metodo nos muestra el nombre del centro en el panel de administración.
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    descripcion = models.CharField(max_length=500, verbose_name="Descripcion")
    duracion = models.IntegerField(verbose_name="Duracion")
    tipo_ejercicio = models.CharField(max_length=200, verbose_name="Tipo de Ejercicio")
    caloria = models.IntegerField(verbose_name="Calorias")
    beneficio = models.CharField(max_length=500, verbose_name="Beneficio")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="actividades")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="actividad"
        verbose_name_plural="actividades"
        ordering=["created"]

    def __str__(self): #Este metodo nos muestra el nombre del centro en el panel de administración.
        return self.nombre



