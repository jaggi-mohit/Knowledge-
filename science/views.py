from engsub.forms import editor, shw
from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Subjects, UserDetail
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from teacherlogin.models import Teacher,Tmsg
from engsub.models import Computer, English, Science, show
from django.core.paginator import Paginator



def home(request):
    user1=request.user
    if request.user.is_anonymous:
        messages.info(request,f'Kindly Login!')
        return redirect('login')
    if user1 is not None:
        obj = English.objects.all()
        obj2= Science.objects.all()
        obj3= Computer.objects.all()
        subjects = Subjects.objects.filter(user_id=user1.id)
        n= UserDetail.objects.get(user_id=user1.id)
        return render(request,'home.html',{'subjects':subjects,'notification':n,'obj':obj,'obj2':obj2,'obj3':obj3})
   

def signup(request):
    if request.method=="GET":
        return render(request,"signup.html")
    
    if request.method=="POST":
        x=request.POST['name1']
        passw1=request.POST['password']
        #passw=make_password(password=passw1, salt=None, hasher='default')
        email=request.POST['email']
        global some_var;
        some_var = request.POST.getlist('checks')
        if User.objects.filter(username=email):
            messages.error(request,f'Email Already Exists!Try Another or Login!')
            return redirect('signup')
        else:
            y=User.objects.create_user(username=email,password=passw1,first_name=x)
            auth.login(request,y)
            z=request.user
            
            data = UserDetail(name=x,user_id=z.id)
            data.save()
            
           
            
            for x2 in some_var:
                userdata=Subjects(subject=x2,username=z,name=x,user_id=z.id)
                userdata.save()
            messages.success(request,f'Welcome {x}! Account Created Kindly Login!')
            return redirect('login')
            
           
        
        
        """
        for x in some_var:
            if x == "English":
                return render(request,'hello.htm')
                """ 
        return render(request,'demo.htm',{'name':x,'math':some_var})
       
     
def login(request):
    if request.method=="POST":
        mail=request.POST['Email']
        passw1=request.POST['password']
        user=auth.authenticate(username=mail,password=passw1)

        print(user)
        if user is not None:
            auth.login(request,user)
            x = request.user
            try:
                isteach= Teacher.objects.get(user_id=x.id)
                if isteach.isteacher == True:
                    messages.info(request,f'Kindly Login from Teacher Login!')
                    return redirect('login')

                else:
                    auth.logout(request)
                    messages.info(request,f'You are not assigned as teacher by admin!')
                    return redirect('login')

            except:
                return redirect('home')

            
        else:
            messages.error(request,f'Invalid Credentials!Try Again!')
            return redirect('login')
    else:

        return render(request,'login.html')





@login_required(login_url='login/')
def showdata(request):
    x = request.user
    if request.method == "POST" and request.FILES['myfiles']:
        myfiles=request.FILES['myfiles']
        fs= FileSystemStorage()
        filename=fs.save(myfiles.name,myfiles)
        url=fs.url(filename)
        uid=request.user
        t = UserDetail.objects.get(user_id=uid.id)
        t.profile_img=url
        t.save()
        

    sb = Subjects.objects.filter(user_id = request.user.id)   
    datas=UserDetail.objects.filter(user=request.user)
    n= UserDetail.objects.get(user_id=x.id)
    return render(request,'profile.html',{'data':datas,'subjects':sb,'notification':n})

def logout(request):
    auth.logout(request)
    messages.info(request,f'Logged Out Successfully!')
    return redirect('login')

def message(request):
    x = request.user
    y = Subjects.objects.filter(user_id=x.id).exclude(message__exact='')
    x1 = Subjects.objects.filter(user_id=x.id)
    n= UserDetail.objects.get(user_id=x)
    n.notif = False
    n.save()
    return render(request,'response.html',{'students':y,'subjects':x1})

def contact(request,pk):
    x = request.user
    
    if request.method == "POST":
        k = Teacher.objects.get(subject=pk)
        k.notifs = True
        k.save()
        y = k.user_id
        z = request.POST['message']
        msg = Tmsg(Fromuser = x,msg=z,user_id=y)
        msg.save()

        messages.info(request,f'Message Sent Successfully')
        return redirect('message')
    n= UserDetail.objects.get(user_id=x.id)
    return render(request,'message2.html',{'notification':n})


def eng(request):
    x = request.user
    sb = Subjects.objects.filter(user_id = request.user.id) 
    sub = Subjects.objects.get(user_id=x.id,subject="English")
    print(sub.subject)
    n= UserDetail.objects.get(user_id=x.id)
    return render(request,'demo.html',{'subjects':sb,'notification':n})


def comps(request):
    x = request.user
    sb = Subjects.objects.filter(user_id = request.user.id) 
    n= UserDetail.objects.get(user_id=x.id)
    return render(request,'demo2.html',{'subjects':sb,'notification':n})

def sci(request):
    x = request.user
    sb = Subjects.objects.filter(user_id = request.user.id) 
    n= UserDetail.objects.get(user_id=x.id)
    return render(request,'demo3.html',{'subjects':sb,'notification':n})

def sub(request):
    x = request.user
    sb = Subjects.objects.filter(user_id = request.user.id)
    obj = English.objects.all()
    paginator =Paginator(obj,1)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        questions= paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions=paginator.page(paginator.num_pages)
    
    n= UserDetail.objects.get(user_id=x.id)
    return render(request,'literature.html',{'obj':obj,'eng':questions,'subjects':sb,'notification':n})
   
def comp(request):
    sb = Subjects.objects.filter(user_id = request.user.id)
    obj = Computer.objects.all()
    c= editor()
    paginator =Paginator(obj,1)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        questions= paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions=paginator.page(paginator.num_pages)
    
    x= request.user
    n= UserDetail.objects.get(user_id=x.id)

    if request.method =="POST":
        x = request.POST['text']
        return render(request,'Computer.html',{'obj':obj,'eng':questions,'subjects':sb,'form':c,'value':x,'notification':n})
       
    

    return render(request,'Computer.html',{'obj':obj,'eng':questions,'subjects':sb,'form':c,'notification':n})

def scie(request):
    sb = Subjects.objects.filter(user_id = request.user.id)
    obj = Science.objects.all()
    paginator =Paginator(obj,1)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        questions= paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions=paginator.page(paginator.num_pages)

    x= request.user
    n= UserDetail.objects.get(user_id=x.id)

    return render(request,'Science.html',{'obj':obj,'eng':questions,'subjects':sb,'notification':n})

def trycode(request,pk):
    k= request.user
    n= UserDetail.objects.get(user_id=k.id)
    sb = Subjects.objects.filter(user_id = request.user.id)
    obj = Computer.objects.get(id=pk)

    if request.method =="POST":
        
        x = request.POST['text']
        s= show.objects.get(id=1)
        s.shws=x
        s.save()
        
        return render(request,'trycode.html',{'code':obj,'subjects':sb,'value':x,'notification':n,'show':s})
    return render(request,'trycode.html',{'subjects':sb,'code':obj,'notification':n})