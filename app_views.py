from django.http import HttpResponse
from django.shortcuts import render

def form(request):
    return render(request, 'form.html')

# Create your views here.
def home(request):
    return HttpResponse('Hello World')

# Create your views here.
def home(request):
    return render(request, 'index.html')
