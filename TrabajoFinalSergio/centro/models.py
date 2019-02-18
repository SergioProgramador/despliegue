from django.db import models

class Centro(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    direccion = models.CharField(max_length=500, verbose_name="Dirección")
    email = models.CharField(max_length=200, verbose_name="Email")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="centros")
    horario = models.CharField(max_length=300, verbose_name="Horario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "centro"
        verbose_name_plural = "centros"
        # Ordenar los centros por fecha de creacion de mas nuevo a mas antiguo.
        ordering = ["-created"]
  
    def __str__(self): #Este metodo nos muestra el nombre del centro en el panel de administración.
        return self.nombre
