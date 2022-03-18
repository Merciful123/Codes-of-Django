"""gs7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from course import views as cv
from fees import views as fv
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cor/', include([
        path('learndj/', cv.learn_django),
        path('learnpy/', cv.learn_python),
    ])),
    path('fe/', include([
        path('feesdj/', fv.fees_django),
        path('feespy/', fv.fees_python),
    ]))
]
