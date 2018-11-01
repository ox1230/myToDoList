from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest

def root(request:HttpRequest):
    return render(request, 'root.html')
