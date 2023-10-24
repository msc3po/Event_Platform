from django import forms
from .models import User

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['profile_image', 'prefix', 'home_address', 'billing_address']