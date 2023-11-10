from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def msdhoni(request):
    return render(request,'msd.html')

def raina(request):
    return HttpResponse('<h1>Suresh Raina is an Indian former international cricketer</h1>')
