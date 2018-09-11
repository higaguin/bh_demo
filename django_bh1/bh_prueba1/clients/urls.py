from django.urls import path
from .views import ClientListView

client_patterns = ([
    path('', ClientListView.as_view(), name='list')
], "clients")