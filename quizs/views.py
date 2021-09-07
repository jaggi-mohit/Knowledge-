from teacherlogin.models import Teacher
from engsub.forms import editor
from django.db.models.aggregates import Max
from science.models import Subjects, UserDetail
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import EngQuiz,SciQuiz,CompQuiz

from django.core.paginator import Paginator


lsteng=[]
anslisteng=[]
answers = EngQuiz.objects.all() 
for i in answers:
    anslisteng.append(i.answer)

lstsci=[]
anslistsci=[]
answers1 = SciQuiz.objects.all() 
for i in answers1:
    anslistsci.append(i.answer)

lstcomp=[]
anslistcomp=[]
answers2 = CompQuiz.objects.all() 
for i in answers2:
    anslistcomp.append(i.answer)




def engquiz(request):
    sb = Subjects.objects.filter(user_id = request.user.id)
    obj = EngQuiz.objects.all()
    paginator =Paginator(obj,1)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        questions= paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions=paginator.page(paginator.num_pages)


    return render(request,'quizeng.html',{'obj':obj,'questions':questions,'subjects':sb})


def sciquiz(request):
    obj = SciQuiz.objects.all()
    sb = Subjects.objects.filter(user_id = request.user.id)

    paginator =Paginator(obj,1)
    x = request.user
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        questions= paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions=paginator.page(paginator.num_pages)
   

    return render(request,'quizsci.html',{'obj':obj,'questions':questions,'subjects':sb})


def compquiz(request):
    obj = CompQuiz.objects.all()
    
    paginator =Paginator(obj,1)
    
    
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        questions= paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions=paginator.page(paginator.num_pages)

    return render(request,'quizcomp.html',{'obj':obj,'questions':questions})


def engresult(request):
    y = request.user
    sb = Subjects.objects.filter(user_id = request.user.id)
    score =0
    try:
        for i in range(len(lsteng)):
            if lsteng[i] == anslisteng[i]:
                score +=1
                print(score)
    except:
        print('hlo')
        lsteng.clear()

    x = Subjects.objects.filter(username=y,user_id=y.id,subject="English")
    for i in x:
        if i.score < score:
            i.score = score
            i.save()
    
    n= UserDetail.objects.get(user_id=y.id)
    return render(request,'result.html',{'score':score,'lst':lsteng,'subjects':sb,'notification':n})

def sciresult(request):
    y = request.user
    sb = Subjects.objects.filter(user_id = request.user.id)
    score =0
    try:
        for i in range(len(lstsci)):
            if lstsci[i] == anslistsci[i]:
                score +=1
    except:
        lstsci.clear()

    x = Subjects.objects.filter(username=y,user_id=y.id,subject="Science")
    for i in x:
        if i.score < score:
            i.score = score
            i.save()
    y= request.user
    n= UserDetail.objects.get(user_id=y.id)
    return render(request,'result.html',{'score':score,'lst':lstsci,'subjects':sb,'notification':n})

def compresult(request):
    y = request.user
    sb = Subjects.objects.filter(user_id = request.user.id)
    score =0
    try:
        for i in range(len(lstcomp)):
            if lstcomp[i] == anslistcomp[i]:
                score +=1
                print(score)
        
    except:
        lstcomp.clear()
        print("hlo")

    x = Subjects.objects.filter(username=y,user_id=y.id,subject="Computer")
    print(score)
    for i in x:
        if i.score < score:
            i.score = score
            i.save()
    y= request.user
    n= UserDetail.objects.get(user_id=y.id)
    return render(request,'result.html',{'score':score,'lst':lstcomp,'subjects':sb,'notification':n})
    
    
    
def engsaveans(request):
    ans= request.GET['ans']
    lsteng.append(ans)
    return HttpResponse("")
    

def scisaveans(request):
    ans= request.GET['ans']
    lstsci.append(ans)
    return HttpResponse("")

def compsaveans(request):
    ans= request.GET['ans']
    lstcomp.append(ans)
    return HttpResponse("")
    

def score(request):
    sb = Subjects.objects.filter(user_id = request.user.id)
    x= request.user
    n= UserDetail.objects.get(user_id=x.id)
    y= Subjects.objects.filter(username=x,user_id=x.id)
    k= Subjects.objects.filter(username=x,subject="Computer",user_id=x.id)
    
    return render(request,'score.html',{'tasks':y,'subjects':sb,'notification':n})

def welcome(request,pk):
    sb = Subjects.objects.filter(user_id = request.user.id)
    y= request.user
    n= UserDetail.objects.get(user_id=y.id)
    lstcomp.clear()
    lstsci.clear()
    lsteng.clear()
    return render(request,'welcome.html',{'sub':pk,'subjects':sb,'notification':n})

def addquiz(request):
    success='False'
    m = request.user
    l = Teacher.objects.get(user_id=m.id)
    if l.isteacher == True:
        if request.method == "POST":
            tt= request.POST['Question']
            op1 = request.POST['Option1']
            op2 = request.POST['Option2']
            op3 = request.POST['Option3']
            op4 = request.POST['Option4']
            ans = request.POST['ans']
            if l.subject == "Computer":
                x = CompQuiz(question=tt,option1=op1,option2=op2,option3=op3,option4=op4,answer=ans)
                x.save()
            if l.subject == "Science":
                x = SciQuiz(question=tt,option1=op1,option2=op2,option3=op3,option4=op4,answer=ans)
                x.save()
            if l.subject == "English":
                x = EngQuiz(question=tt,option1=op1,option2=op2,option3=op3,option4=op4,answer=ans)
                x.save()
            success='True'
            return render(request,'addquiz.html',{'success':success,'notification':l})
    else:
        success='False1'
        return render(request,'addquiz.html',{'success':success})
    
    return render(request,'addquiz.html',{'success':success,'subject':l.subject,'notification':l})
