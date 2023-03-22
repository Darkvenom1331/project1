from django.http import HttpResponse
from django.shortcuts import render
 #Create your views here.
def index(request):
    return render(request,"hello/index.html")

def kiki(request):
    return HttpResponse("jeni krishnan")

def krishnan(request):
    return HttpResponse("i love krishnnan")

def strings(request,name):
    return render(request,"hello/strings.html",{
        "name":name
    })
    