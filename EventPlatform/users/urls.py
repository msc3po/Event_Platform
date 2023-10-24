
from django.urls import path
from . import views

urlpatterns = [
  path('account_settings/', views.user_account_settings, name='account_settings')
]