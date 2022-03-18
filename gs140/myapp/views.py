from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .forms import LoginForm
# Create your views here.

class MyLoginView(LoginView):
 template_name='myapp/login.html'
 authentication_form=LoginForm

class MyLogoutView(LogoutView):
 template_name='myapp/logout.html'

class MyPasswordChangeView(PasswordChangeView):
 template_name='myapp/changepass.html'
 success_url='/changepassdone/'

class MyPasswordChangeDoneView(PasswordChangeDoneView):
 template_name='myapp/changepassdone.html'
