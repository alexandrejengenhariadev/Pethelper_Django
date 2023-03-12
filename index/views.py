from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloworld(request):
    return HttpResponse('Hello world!')
def principal(request):
    return render(request, 'index/index.html')
