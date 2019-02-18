from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Inscripcion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellidos = models.CharField(max_length=150, verbose_name="Apellidos")
    dni = models.CharField(max_length=100, verbose_name="DNI")
    edad = models.IntegerField( verbose_name="Edad")
    telefono = models.IntegerField(verbose_name="Teléfono")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    cuenta_bancaria = models.CharField(max_length=200, verbose_name="Cuenta Bancaria")
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False)
    cuota = models.IntegerField(default=30, verbose_name="Cuota")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Inscripción"
        verbose_name_plural="Inscripciones"
        ordering=['created']

    def save(self, **kwargs):
        if kwargs is not None and 'request' in kwargs and self.user is None:
            request = kwargs.pop('request')
            self.user = request.user
        super().save(**kwargs)

    def __str__(self):
        return self.nombre

