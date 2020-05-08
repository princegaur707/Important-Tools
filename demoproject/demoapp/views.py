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
    try:
        ans=str(a/b)
        return HttpResponse(ans)
    except:
        return HttpResponse("Cannot Divide by 0")

def calculate(request,eq):
    return HttpResponse(eval(eq))