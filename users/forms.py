from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField() # default required=True
    phone_number = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

        widgets = {
            'phone_number': PhoneNumberPrefixWidget(attrs={'class': 'form-control','placeholder': '71234***'}, initial='NG')
        }

