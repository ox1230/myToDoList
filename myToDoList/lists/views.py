from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from lists.models import ToDo

def root(request:HttpRequest):

    return render(request, 'root.html', 
        {'list_of_todo': ToDo.objects.all()})

def add_todo(request:HttpRequest):
    if request.method == 'POST':
        ToDo.objects.create(text = request.POST['todo_text'])
        return redirect('root')
