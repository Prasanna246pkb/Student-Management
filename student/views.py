from django.shortcuts import render
from student.models import Student
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'studentlist.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','course','marks','fee']
    template_name = 'createstudent.html'
    success_url = reverse_lazy('list_stud')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','email','course','marks']
    template_name = 'updatestudent.html'
    success_url = reverse_lazy('list_stud')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'deletestudent.html'
    success_url = reverse_lazy('list_stud')