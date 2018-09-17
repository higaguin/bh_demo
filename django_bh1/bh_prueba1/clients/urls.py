from django.urls import path
from .views import ClientListView, ClientUpdate

client_patterns = ([
    path('', ClientListView.as_view(), name='list'), 
    path('update/<int:pk>', ClientUpdate.as_view(), name="update"),
], "clients")