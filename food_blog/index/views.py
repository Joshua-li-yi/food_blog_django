from django.shortcuts import render

# Create your views here.

# 起始页
def index(request):
    return render(request, 'index.html')

# 注册
def sigup(request):
    return render(request, 'signup.html')

# 登陆
def logIn(request):
    return render(request, 'logIn.html')

# test
def test(request):
    return render(request, 'test.html')




