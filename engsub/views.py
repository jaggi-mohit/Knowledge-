from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render
from .models import Computer, English, Science,show
from science.models import Subjects
from teacherlogin.models import Teacher
from .forms import editor,edit
import requests
import bs4

@login_required(login_url='login/')
def addcontent(request):
    success='False'
    m = request.user
    l = Teacher.objects.get(user_id=m.id)
    c = editor()
    k= edit()
    if l.isteacher == True:
        if request.method == "POST":
            tt= request.POST['titles']
            vid = request.POST['videos']
            td = request.POST['tdesc']
            if l.subject == "English":
                x = English(title=tt,video=vid,desc=td)
                x.save()
            if l.subject == "Science":
                x = Science(title=tt,video=vid,desc=td)
                x.save()
            if l.subject == "Computer":
                y= request.POST['code']
                z=request.POST['desc']
                
                x = Computer(title=tt,video=vid,desc=z,code=y)
                x.save()
                
            success='True'
            return render(request,'addcontent.html',{'success':success})
    else:
        success='False1'
        return render(request,'addcontent.html',{'success':success})
    
    return render(request,'addcontent.html',{'success':success,'subject':l.subject,'form':c,'forms':k,'notification':l})

@login_required(login_url='login/') 
def show(request):
    x = request.user
    y = Teacher.objects.get(user_id=x.id)
    if y.subject == "English":
        z = English.objects.all()
        return render(request,'yourcontent.html',{'tasks':z,'notification':y})
    if y.subject == "Science":
        z = Science.objects.all()
        return render(request,'yourcontent.html',{'tasks':z,'notification':y})
    if y.subject == "Computer":
        z = Computer.objects.all()
        return render(request,'yourcontent.html',{'tasks':z,'notification':y})
    
    return redirect('yourcontent')



def search(request):
    user1 = request.user
    subjects = Subjects.objects.filter(user_id=user1.id)
    word=request.GET['word']
    print(word)
    
    if word =="":
        return redirect('search')
    res = requests.get('https://www.dictionary.com/browse/'+word)
    res2 = requests.get('https://www.thesaurus.com/browse/'+word)
    

    if res:
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        meaning = soup.find_all('div', {'value': '1'})
        meaning1 = meaning[0].getText()
    else:
        word = 'Sorry, '+ word + ' Is Not Found In Our Database'
        meaning = ''
        meaning1 = ''

    if res2:
        soup2 = bs4.BeautifulSoup(res2.text, 'lxml')

        synonyms = soup2.find_all('a',{'class': 'css-1gyuw4i eh475bn0'})
        ss = []
        for b in synonyms[:10]:
            re = b.text.strip()
            ss.append(re)
        se = ss
        

        

        antonyms = soup2.find_all('a', {'class': 'css-pc0050 eh475bn0'})
        aa = []
        for c in antonyms[0:]:
            r = c.text.strip()
            aa.append(r)
        ae = aa
    else:
        se = ''
        ae = ''


    results = {
        'word' : word,
        'meaning' : meaning1,

    }


    return render(request, 'search.html', {'se': se, 'ae': ae, 'results': results,'subjects':subjects})

def dict(request):
    user1= request.user
    subjects = Subjects.objects.filter(user_id=user1.id)
    return render(request,'search.html',{'subjects':subjects})