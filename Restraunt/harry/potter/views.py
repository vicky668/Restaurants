from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse('This is The Restraunt Management System')

def vicky (request):
    return render(request,'index.html')    