from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'second_adress', 'city', 'rfc', 'phone', 'mobile', 'email', 'website']
        widgets = {
            'name': forms.Textarea(attrs={'class':'validate'}),
            'address': forms.Textarea(attrs={'class':'validate', 'rows':3}),
            'second_adress': forms.Textarea(attrs={'class':'validate', 'rows':3}),
            'city': forms.Textarea(attrs={'class':'validate'}),
            'rfc': forms.Textarea(attrs={'class':'validate'}),
            'mobile': forms.Textarea(attrs={'class':'validate'}),
            # 'email': forms.EmailField(attrs={'class':'validate'}),
            'website': forms.URLInput(attrs={'class':'validate'}),
        }