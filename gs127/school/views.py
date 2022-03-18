from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
# Create your views here.

class StudentCreateView(CreateView):
 model = Student
 fields = ['name', 'email', 'password']
 # success_url = '/thanks/'
 template_name = 'school/sform.html'

class ThanksTemplteView(TemplateView):
 template_name = 'school/thanks.html'

class StudentDetailView(DetailView):
 model = Student