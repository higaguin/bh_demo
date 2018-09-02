from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.
class UserAccountView(TemplateView):
    template_name = "user/user_account.html"