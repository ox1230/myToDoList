from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from lists.models import ToDo
from datetime import date, datetime
def root(request:HttpRequest):

        list_of_todo = list(ToDo.objects.filter(completed = False).exclude(due = None).order_by('-priority','due')) +\
                                list(ToDo.objects.filter(completed = False, due = None).order_by('-priority'))
        
        lot = []
        for todo in list_of_todo:
                if todo.due == None:
                        lot.append((todo,None))
                else:
                        lot.append( (todo,date.strftime(todo.due,"%Y-%m-%d")) )
        
        return render(request, 'root.html', 
                #먼저 due가 있는 것들을 오름차순 정렬, 뒤에 due가 없는 것들 정렬
                {'list_of_todo': lot  , 
                'list_of_todo_completed' : list(ToDo.objects.filter(completed = True).exclude(due = None).order_by('due')) +
                                                list(ToDo.objects.filter(completed = True, due = None).order_by('due')),
                'today' : date.today()})

def add_todo(request:HttpRequest):
        if request.method == 'POST':
                if request.POST['todo_due']: due = datetime.strptime(request.POST['todo_due'],"%Y-%m-%d")
                else: due = None
                temp = ToDo(text = request.POST['todo_text'], 
                        priority = request.POST['todo_priority'],
                        due = due,      
                )

                temp.save()
                return redirect('root')
def complete_todo(request:HttpRequest):
        if request.method == 'POST':
                temp = ToDo.objects.get(id = request.POST['id'])
                temp.completed = True
                temp.save()
                return redirect('root')

def uncomplete_todo(request:HttpRequest):
        if request.method == 'POST':
                temp = ToDo.objects.get(id = request.POST['id'])
                temp.completed = False
                temp.save()
                return redirect('root')



def delete_todo(request:HttpRequest):
        if request.method == 'POST':
                temp = ToDo.objects.get(id = request.POST['id'])
                temp.delete()
                return redirect('root')

def edit_todo(request:HttpRequest):
        if request.method == "POST":
                data = request.POST
                temp = ToDo.objects.get(id = data['id'])
                temp.text = data['todo_text']
                temp.priority = data['todo_priority']
                if data['todo_due'] != "" : temp.due = datetime.strptime(data['todo_due'], "%Y-%m-%d")
                temp.save()

                return redirect('root')