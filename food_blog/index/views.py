from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def sigup(request):
    return render(request, 'signup.html')


def logIn(request):
    return render(request, 'logIn.html')


def home(request):
    return render(request, 'home.html')


def write_blog(request):
    return render(request, 'writeblog.html')

def me(request):
    return render(request, 'me.html')