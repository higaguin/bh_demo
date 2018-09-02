from django.urls import path
from .views import UserAccountView

user_patterns = ([
    path('', UserAccountView.as_view(), name='user_account'),
], "user")
