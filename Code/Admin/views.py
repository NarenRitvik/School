from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("<h1>Login</h1>");
