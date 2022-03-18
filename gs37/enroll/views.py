from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST)
  if fm.is_valid():
   print('Form Validated')
   name = fm.cleaned_data['name']
   email = fm.cleaned_data['email']
   password = fm.cleaned_data['password']
   print('Name:', name)
   print('Email:', email)
   print('Password:', password)
   fm = StudentRegistration()
   
 else:
  fm = StudentRegistration()

 return render(request, 'enroll/userregistration.html', {'form':fm})
