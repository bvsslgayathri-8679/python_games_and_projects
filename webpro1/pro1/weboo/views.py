from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def intro(request):
    return render(request,'intro.html')
def lists(request):
    return render(request,'lists.html')
def tables(request):
    return render(request,'tables.html')
def fontsandimages(request):
    return render(request,'fontsandimages.html')
