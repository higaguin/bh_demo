from django.shortcuts import render, HttpResponse
from .models import Company
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy
from .forms import CompanyForm

# Create your views here.
class ClientListView(ListView):
    model = Company
    template_name = 'clients/company_list.html'
    # paginate_by = 2

class ClientUpdate(UpdateView):
    form_class = CompanyForm
    model = Company
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('clients:update', args=[self.object.id]) + '?ok'