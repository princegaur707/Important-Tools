from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Prince")

def add(request,a,b):
    ans = str(a+b)
    return HttpResponse(ans)

def multiply(request,a,b):
    ans= str(a*b)
    return HttpResponse(ans)

def divide(request,a,b):
    ans=str(a/b)
    return HttpResponse(ans)