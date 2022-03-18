from django.shortcuts import render
from datetime import datetime
# Create your views here.

#Example 1
def learn_django(request):
  return render(request, 'course/courseone.html', {'nm':'Django'})

"""
  #Example 2
  def learn_django(request):
    cname = 'Django'
    duration = '4 Months'
    seats = 10
    django_details = {'nm':cname, 'du':duration, 'st':seats}
    return render(request, 'course/courseone.html', django_details)
"""
"""
  #Example 3
  def learn_django(request):
    return render(request, 'course/courseone.html', {'nm':'Django is awesome'})
"""
"""
  #Example 4
  def learn_django(request):
    d = datetime.now()
    return render(request, 'course/courseone.html', {'dt':d})
"""
"""
  #Example 5
  def learn_django(request):
    return render(request, 'course/courseone.html', {'p1':56.24321, 'p2':56.000, 'p3':56.37000})
"""
"""
  #Example 6
  def learn_django(request):
    return render(request, 'course/courseone.html', {'nm':True})
"""
"""
  #Example 7
  def learn_django(request):
    return render(request, 'course/courseone.html', {'nm':'Django'})
"""
"""
  #Example 8
  def learn_django(request):
    return render(request, 'course/courseone.html', {'nm':'Django', 'st':5})
"""
"""
#Example 9
def learn_django(request):
  student = {'names': ['Rahul', 'Sonam', 'Raj','Anu']}
  return render(request, 'course/courseone.html', student)
"""
"""
#Example 10
  def learn_django(request):
    stu = {'stu1': {'name': 'Rahul', 'roll':101},
            'stu2': {'name': 'Sonam', 'roll':102},
            'stu3': {'name': 'Raj', 'roll':103},
            'stu4': {'name': 'Anu', 'roll':104},
          }
    students = {'student':stu}
    return render(request, 'course/courseone.html', students)
"""
"""
  #Example 11
  def learn_django(request):
    data = {'name': 'Rahul', 'roll':101}
    return render(request, 'course/courseone.html', {'data':data})
"""

"""
  #Example 12
  def learn_django(request):
    data = {'stu1': {'name': 'Rahul', 'roll':101},
              'stu2': {'name': 'Sonam', 'roll':102},
              'stu3': {'name': 'Raj', 'roll':103},
              'stu4': {'name': 'Anu', 'roll':104},
            }
    return render(request, 'course/courseone.html', {'data':data})
"""