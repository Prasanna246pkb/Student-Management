"""
URL configuration for studentMangament project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from student.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',StudentListView.as_view(), name = 'list_stud'),
    path('createstudent/',StudentCreateView.as_view(), name = 'create_stud'),
    path('updatestudent/<int:pk>/',StudentUpdateView.as_view(), name = 'update_stud'),
    path('deletestudent/<int:pk>/',StudentDeleteView.as_view(), name = 'delete_stud')
]
