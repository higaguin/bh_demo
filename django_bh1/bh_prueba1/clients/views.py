from django.shortcuts import render
from .models import Company
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .forms import CompanyForm

# Create your views here.
class ClientListView(ListView):
    model = Company
    template_name = 'clients/company_list.html'
    # paginate_by = 2

class ClientUpdate(UpdateView):
    model = Company
    fields = ['name', 'address', 'second_adress']
    template_name_suffix = '_update_form'