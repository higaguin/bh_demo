from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    address = models.TextField(verbose_name="Dirección")
    second_adress = models.TextField(verbose_name="Segunda Dirección")
    city = models.CharField(verbose_name="Ciudad", max_length=200)
    rfc = models.CharField(verbose_name="RFC", max_length=13)
    phone = models.CharField(verbose_name="Teléfono", max_length=24)
    mobile = models.CharField(verbose_name="Teléfono Móvil", max_length=24)
    email = models.CharField(verbose_name="Correo Electrónico", max_length=200)
    website = models.CharField(verbose_name="Página Web", max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "compañía"
        verbose_name_plural = "compañías"
        ordering = ['created', 'name']

    def __str__(self):
        return self.name