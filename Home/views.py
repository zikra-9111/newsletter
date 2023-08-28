from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'home.html')   

def about(request):
    return HttpResponse("hello this my about page ")

def services(request):
    return HttpResponse("hello this my service page")

def contact(request):
    return HttpResponse("hello this my contact")

