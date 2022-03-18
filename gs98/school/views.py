from django.shortcuts import render
from .models import Student
from datetime import date, time
# Create your views here.

def home(request):
 student_data = Student.objects.all()
 # student_data = Student.objects.filter(name__exact='Sonam')
 # student_data = Student.objects.filter(name__iexact='sonam')
 # student_data = Student.objects.filter(name__contains='u')
 # student_data = Student.objects.filter(name__icontains='U')
 # student_data = Student.objects.filter(id__in = [1, 5, 7])
 # student_data = Student.objects.filter(marks__in = [60, 70])
 # student_data = Student.objects.filter(marks__gt = 60)
 # student_data = Student.objects.filter(marks__gte = 60)
 # student_data = Student.objects.filter(marks__lt = 60)
 # student_data = Student.objects.filter(marks__lte = 60)
 # student_data = Student.objects.filter(name__startswith='S')
 # student_data = Student.objects.filter(name__istartswith='s')
 # student_data = Student.objects.filter(name__endswith='L')
 # student_data = Student.objects.filter(name__iendswith='L')
 # student_data = Student.objects.filter(passdate__range=('2020-04-01', '2020-05-03'))
 # student_data = Student.objects.filter(admdatetime__date=date(2020, 1, 2))
 # student_data = Student.objects.filter(admdatetime__date__gt=date(2020, 1, 4))
 # student_data = Student.objects.filter(passdate__year=2019)
 # student_data = Student.objects.filter(passdate__year__gte=2019)
 # student_data = Student.objects.filter(passdate__month=4)
 # student_data = Student.objects.filter(passdate__month__gte=4)
 # student_data = Student.objects.filter(passdate__day=2)
 # student_data = Student.objects.filter(passdate__day__gt=2)
 # student_data = Student.objects.filter(passdate__week=14)
 # student_data = Student.objects.filter(passdate__week__gt=14)
 # student_data = Student.objects.filter(passdate__week_day=5)
 # student_data = Student.objects.filter(passdate__week_day__gt=5)
 # student_data = Student.objects.filter(passdate__quarter=2)
 # student_data = Student.objects.filter(admdatetime__time__gt=time(21,17))
 # student_data = Student.objects.filter(admdatetime__hour__gt=5)
 # student_data = Student.objects.filter(admdatetime__minute__gt=20)
 # student_data = Student.objects.filter(admdatetime__second__gt=20)
 # student_data = Student.objects.filter(roll__isnull=False)




 print("Return:", student_data)
 print()
 print("SQL Query:", student_data.query)
 return render(request, 'school/home.html', {'students':student_data})
