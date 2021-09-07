from science.models import Subjects, UserDetail
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Teacher, Tmsg
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

def admin(request):
    return render(request,'adminlogin.html')

def teacherlogin(request):
    if request.method=="POST":
        mail=request.POST['Email']
        passw1=request.POST['password']
        user=auth.authenticate(username=mail,password=passw1)

        print(user)
        if user is not None:
            auth.login(request,user)
            x = request.user
            print(x.id)
            try:
                isteach= Teacher.objects.get(user_id=x.id)
                if isteach.isteacher == True:
                    return redirect('teacherhome')
                    
                else:
                    auth.logout(request)
                    messages.info(request,f'Not set as teacher kindly contact admin!')
                    return redirect('adminlog')
            except:
                auth.logout(request)
                messages.info(request,f'Not Teacher! Kindly Login From Student Login!')
                return redirect('adminlog')
        else:
            messages.error(request,f'Invalid Credentials!Try Again!')
            return redirect('adminlog')
    else:

        return render(request,'adminlog.html')

@login_required(login_url='login/')
def teacherhome(request):
    x = request.user
    y = Teacher.objects.get(user_id=x.id)
    return render(request,'teacherhome.html',{'notification':y})


@login_required(login_url='adminlog/')
def tprofile(request):
    x= request.user
    if request.method == "POST" and request.FILES['myfiles']:
        myfiles=request.FILES['myfiles']
        fs= FileSystemStorage()
        filename=fs.save(myfiles.name,myfiles)
        url=fs.url(filename)
        uid=request.user
        t = Teacher.objects.get(user_id=uid.id)
        t.profile_img=url
        t.save()
        

    y = Teacher.objects.get(user_id=x.id)
    datas=Teacher.objects.filter(user=request.user)
    return render(request,'tprofile.html',{'data':datas,'notification':y})

@login_required(login_url='adminlog/')
def student(request):
    i = request.user
    try:
        t = Teacher.objects.get(user_id=i.id)
        sub = t.subject
        x = Subjects.objects.filter(subject=sub)

    except:
        messages.info(request,f'Not Teacher you cannot access!')
        return redirect('login')
    
    return render(request,'student.html',{'students':x,'notification':t})


@login_required(login_url='login/')
def contact(request,pk):
    success='False'
    current_user = request.user
    x = Teacher.objects.get(user_id=current_user.id)
    sub = x.subject
    if request.method == 'POST':

        
        desc=request.POST['message']
        
        try:
            ins=Subjects.objects.get(subject=sub,username=pk)
            x = ins.user_id
            name1 = ins.name
            msg = Subjects(message=desc,user_id=x,name=name1,username=pk,teacher=current_user.first_name,subjectincharge=sub)
            msg.save()
            n= UserDetail.objects.get(user_id=x)
            n.notif = True
            n.save()
            success='True'
            messages.info(request,f'Message Sent Successfully!')
            return redirect('student')
        
        except:
            messages.info(request,f'User Doesnot exist!')
            return redirect('student')
    return render(request,'message.html',{'success':success,'notification':x})

@login_required(login_url='login/')
def remove(request,pk):
    item = Subjects.objects.get(id=pk)
    item.delete()
    return redirect('message')

def msg(request):
    x = request.user
    y = Tmsg.objects.filter(user_id=x.id)
    z = Teacher.objects.get(user_id=x.id)
    z.notifs = False
    z.save()
    return render(request,'tmsg.html',{'students':y})

def delte(request,pk):
    print(pk)
    item = Tmsg.objects.get(id=pk)
    item.delete()
    return redirect('msgs')