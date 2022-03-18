from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView
from django import forms

from .forms import StudentForm
# Create your views here.

# class StudentCreateView(CreateView):
#  model = Student
#  fields = ['name', 'email', 'password']
#  success_url = '/thanks/'

#  def get_form(self):
#   form = super().get_form()
#   form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
#   form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
#   return form

class StudentCreateView(CreateView):
 form_class = StudentForm
 template_name = 'school/student_form.html'
 success_url = '/thanks/'

class ThanksTemplteView(TemplateView):
 template_name = 'school/thanks.html'
