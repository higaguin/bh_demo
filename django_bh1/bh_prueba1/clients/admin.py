from django.contrib import admin
from .models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Company, CompanyAdmin)