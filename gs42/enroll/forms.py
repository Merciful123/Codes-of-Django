from django.core import validators
from django import forms
class StudentRegistration(forms.Form):
 name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
 email=forms.EmailField()