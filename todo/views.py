from science.models import Subjects, UserDetail
from django.shortcuts import render,redirect
from .models import Todo
from django.contrib.auth.models import User

def todo(request):
    current_user = request.user
    n= UserDetail.objects.get(user_id=current_user.id)
    x = Subjects.objects.filter(user_id=current_user.id)
    return render(request,'todo.html',{'subjects':x,'notification':n})

def addtask(request):
    success='False'
    current_user = request.user
    n= UserDetail.objects.get(user_id=current_user.id)
    x = Subjects.objects.filter(user_id=current_user.id)
    if request.method == 'POST':
        taskname=request.POST['taskname']
        taskdesc=request.POST['taskdesc']
        
        print(current_user.id)
        ins=Todo(tasktitle=taskname,taskdesc=taskdesc,user_id=current_user.id)
        ins.save()
        success='True'
        return render(request,'addtask.html',{'success':success,'subjects':x,'notification':n})
    return render(request,'addtask.html',{'success':success,'subjects':x,'notification':n})

def yourtask(request):
    current_user=request.user
    n= UserDetail.objects.get(user_id=current_user.id)
    alltasks = Todo.objects.filter(user_id=current_user.id)
    
    x = Subjects.objects.filter(user_id=current_user.id)
    return render(request,'yourtask.html',{'tasks':alltasks,'subjects':x,'notification':n})

def remove(request, pk):
    item = Todo.objects.get(id=pk)
    item.delete()
    return redirect('http://127.0.0.1:8000/home/todo/yourtask')