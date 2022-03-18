from django.shortcuts import render

# Create your views here.
def home(request):
 context = {'data':'Hello I am Geeky Shows. I am teaching Django. I am looking for Sonam'}
 return render(request, 'myapp/home.html', context)