from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from django.views.generic.base import TemplateView
from .forms import StudentForm
# Create your views here.

class StudentCreateView(CreateView):
 form_class = StudentForm
 template_name = 'school/student_form.html'
 success_url = '/thanks/'

class StudentUpdateView(UpdateView):
 model = Student
 form_class = StudentForm
 template_name = 'school/student_form.html'
 success_url = '/thanksupdate/'

class StudentDeleteView(DeleteView):
  model = Student
  success_url = '/thanksdelete/'
  template_name = 'school/studel.html'

class ThanksTemplateView(TemplateView):
 template_name = 'school/thanks.html'

class ThanksUpdateTemplateView(TemplateView):
 template_name = 'school/thanksupdate.html'

class ThanksDeleteTemplateView(TemplateView):
 template_name = 'school/thanksdelete.html'