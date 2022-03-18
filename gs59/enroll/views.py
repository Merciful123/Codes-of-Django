from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.
def regi(request):
  messages.info(request, 'Now You can Login')
  messages.success(request, 'Update ho gaya hai')
  messages.warning(request, 'This is warning')
  messages.error(request, 'This is an error')
  fm = StudentRegistration()
  return render(request, 'enroll/userregistration.html', {'form':fm})