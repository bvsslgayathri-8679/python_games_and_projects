from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Gayathri'})
def add(request):
    v1=request.POST['num1']
    v2=request.POST['num2']
    res=int(v1)+int(v2)
    return render(request,'result.html',{'result':res})
