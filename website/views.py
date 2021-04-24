from django.shortcuts import render, HttpResponse, render
from django.template import loader


# Create your views here.




def home (request):
    return render(request, 'home.html')



def login (request):
    return render(request, 'login.html')


def signup (request):
    return render(request, 'signup.html')

def about (request):
    return render(request, 'about.html')

def contact (request):
    return render(request, 'contact.html')

def logout (request):
    return render(request, 'logout.html')
