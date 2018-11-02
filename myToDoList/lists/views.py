from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from lists.models import ToDo

def root(request:HttpRequest):

    return render(request, 'root.html', 
        {'list_of_todo': ToDo.objects.filter(completed = False).order_by('-priority'),
        'list_of_todo_completed' : ToDo.objects.filter(completed = True)})

def add_todo(request:HttpRequest):
        if request.method == 'POST':
                temp = ToDo(text = request.POST['todo_text'], 
                        priority = request.POST['todo_priority'])

                temp.save()
                return redirect('root')
def complete_todo(request:HttpRequest):
        if request.method == 'POST':
                temp = ToDo.objects.get(id = request.POST['id'])
                temp.completed = True
                temp.save()
                return redirect('root')


def delete_todo(request:HttpRequest):
        if request.method == 'POST':
                temp = ToDo.objects.get(id = request.POST['id'])
                temp.delete()
                return redirect('root')