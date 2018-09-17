from django import forms
from .models import Company
from django.utils.translation import gettext as _

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'second_adress', 'city', 'rfc', 'phone', 'mobile', 'email', 'website']
        widgets = {
            'name': forms.TextInput(attrs={'class':'validate'}),
            'address': forms.Textarea(attrs={'class':'materialize-textarea'}),
            'second_adress': forms.Textarea(attrs={'class':'materialize-textarea'}),
            'city': forms.TextInput(attrs={'class':'validate'}),
            'rfc': forms.TextInput(attrs={'class':'validate'}),
            'mobile': forms.TextInput(attrs={'class':'validate phone'}),
            'email': forms.EmailInput(attrs={'class':'validate'}),
            'website': forms.URLInput(attrs={'class':'validate'}),
        }
        labels = { 
            'address': _('Dirección'), 
            'addsecond_adressress': _('Segunda Dirección'), 
            'city': _('Ciudad'), 
            'rfc': _('RFC'), 
            'mobile': _('Celular'), 
            'email': _('Correo Electrónico'), 
            'website': _('Sitio Web'), 
        }