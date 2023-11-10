from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohit(request):
    return render(request,'rohit.html')

def bumrah(request):
    return HttpResponse('<h1>Bumrah is currently considered one of the best bowlers in the world</h1>')