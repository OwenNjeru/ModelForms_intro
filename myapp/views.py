from django.shortcuts import render
from myapp.forms import StudentForm


# Create your views here.

def home(request):
    mimi = StudentForm
    return render(request, 'index.html',{'form':mimi})
