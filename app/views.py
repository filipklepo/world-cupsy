from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('index')

@login_required(login_url='login')
def vote(request):
    return HttpResponse("Vote here!")