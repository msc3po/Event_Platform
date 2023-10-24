
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path('account_settings/', views.user_account_settings, name='account_settings'),
  path('accounts/', include('django.contrib.auth.urls'))

]