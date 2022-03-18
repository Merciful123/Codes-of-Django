from django.core import validators
from django import forms

def starts_with_s(value):
 if value[0] != 's':
  raise forms.ValidationError('Name should start with s')

class StudentRegistration(forms.Form):
 name = forms.CharField(validators=[starts_with_s])
 email=forms.EmailField()