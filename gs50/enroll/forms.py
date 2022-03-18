from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
 name = forms.CharField(max_length=50, required=False)
 class Meta:
  model = User
  fields = ['name', 'password', 'email']
  labels = {'name':'Enter Name', 'password':'Enter Password', 'email': 'Enter EMail'}
  widgets = {'password':forms.PasswordInput }

