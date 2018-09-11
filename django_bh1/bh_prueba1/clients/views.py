from django.shortcuts import render
from .models import Company
from django.views.generic.list import ListView

# Create your views here.
class ClientListView(ListView):
    model = Company
    template_name = 'clients/company_list.html'
    # paginate_by = 2