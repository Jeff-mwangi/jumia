from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # required=True by default
    # phone_number input
    phone_number = forms.CharField()
    
    class Meta:
        model = User  
        fields = ['username', 'email','phone_number', 'password1', 'password2'] # fields to be shown in the form

    # widgets
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Phone Number'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})

    def clean_password2(self, *args,**kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2 :
            raise forms.ValidationError("Password does not match")
        return password2
