from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def sigup(request):
    return render(request, 'signup.html')