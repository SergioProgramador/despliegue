from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    #descripcion = models.CharField(max_length=500, verbose_name="Descripción")
    descripcion = RichTextUploadingField(max_length=800, verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="rutinas")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="ejercicio"
        verbose_name_plural="ejercicios"
        ordering=["created"]

    def __str__(self):
        return self.nombre
   

class Rutina(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.CharField(max_length=500, verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="ejercicios")
    ejercicios=models.ManyToManyField(Ejercicio, verbose_name="Ejercicios")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="rutina"
        verbose_name_plural="rutinas"
        ordering=["created"]

    def __str__(self):
        return self.titulo

class RutinaPersonalizada(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = RichTextUploadingField(max_length=500, verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="ejercicios")
    ejercicios=models.ManyToManyField(Ejercicio, verbose_name="Ejercicios", related_name='ejer')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="rutinasPersonalizada"
        verbose_name_plural="rutinasPersonalizada"
        ordering=["created"]

    def __str__(self):
        return self.titulo