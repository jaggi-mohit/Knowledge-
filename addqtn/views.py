from teacherlogin.models import Teacher
from science.models import Subjects, UserDetail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from addqtn.models import showdata,ans

@login_required(login_url='login/')
def addqtn(request):
    if request.method == "POST":
        x = request.user
       
        qtn= request.POST['txtarea']
        y = showdata(question=qtn,username=x)
        y.save()
        return redirect('home')

@login_required(login_url='login/')
def qtnans(request):
    user1 = request.user
    n= UserDetail.objects.get(user_id=user1.id)
    datas=showdata.objects.all()
    ans1= ans.objects.all()
    subjects = Subjects.objects.filter(user_id=user1.id)
    x= Teacher.objects.all()
    return render(request,'qtnans.html',{'ans': datas,'ans1':ans1,'user':user1,'subjects':subjects,'teacher':x,'notification':n})

@login_required(login_url='login/')
def addans(request,pk):
    x = request.user
    n= UserDetail.objects.get(user_id=x.id)
    subjects = Subjects.objects.filter(user_id=x.id)
    if request.method =="POST":
        
        answ = request.POST['txtarea']
        y = ans(username=x,answers=answ,qtn_id=pk)
        y.save()
        
        messages.info(request,f'Answer is added successfully!')
        return redirect('qtnans')
        
    return render(request,'addans.html',{'add':pk,'subjects':subjects,'notification':n})

@login_required(login_url='login/')
def delqtn(request,pk):
    item = showdata.objects.get(id=pk)
    item.delete()
    messages.info(request,f"Question is been Deleted Successfully!")
    return redirect('qtnans')

@login_required(login_url='login/')
def edit(request,pk):
    x = request.user
    n= UserDetail.objects.get(user_id=x.id)
    item = ans.objects.get(id=pk)
    if request.method == "POST":
        x = request.POST['txtarea']
        item.answers = x
        item.save()
        messages.info(request,f"Answer Edited Successfully!")
        return redirect('qtnans')
    return render(request,'addans.html',{'data':pk,'val':item.answers,'notification':n})

def delete(request,pk):
    item = ans.objects.get(id=pk)
    item.delete()
    messages.info(request,f"Answer Deleted Successfully!")
    return redirect('qtnans')


def showqtn(request):
    x = request.user
    n= UserDetail.objects.get(user_id=x.id)
    y = showdata.objects.filter(username=x)
    ans1= ans.objects.all()
    user1 = request.user
    subjects = Subjects.objects.filter(user_id=user1.id)
    return render(request,'showqtn.html',{'qtn':y,'ans1':ans1,'user':user1,'subjects':subjects,'notification':n})