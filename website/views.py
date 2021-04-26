from django.shortcuts import render, HttpResponse, render, redirect
from django.template import loader
from .forms import RegisterForm


# Create your views here.




def home (request):
    return render(request, 'home.html')



def login (request):
    return render(request, 'login.html')



def about (request):
    return render(request, 'about.html')

def contact (request):
    return render(request, 'contact.html')

def signout (request):
    return render(request, 'logout.html')


def signup (response):

    if response.method =="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('home')
    


    else:
        form = RegisterForm()

    return render(response, 'signup.html', {"form": form})



def profile(request):
    
    return render(request, 'profile.html')

