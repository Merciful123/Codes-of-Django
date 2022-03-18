from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
 
 student_data = Student.objects.all()[:5]
 # student_data = Student.objects.all()[5:10]
 # student_data = Student.objects.all()[:11:2]
 

 print("Return:", student_data)
 print()
 print("SQL Query:", student_data.query)
 return render(request, 'school/home.html', {'students':student_data })
