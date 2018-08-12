from django.db import models

# Create your models here.
class Modulos(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion")
    icon = models.CharField(max_length=200, verbose_name="Icono")
    order = models.IntegerField(verbose_name="Orden")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "modulo"
        verbose_name_plural = "modulos"

    def __str__(self):
        return self.name