from django.contrib import admin
from .models import Modulos

# Register your models here.
class ModulosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'description', 'order')
    search_fields = ('name',)

admin.site.register(Modulos, ModulosAdmin)