"""knowledge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, messages
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from science import views as v1
from todo import views as v2
from teacherlogin import views as v3
from engsub import views as v4
from addqtn import views as v5
from quizs import views as v6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.signup,name='signup'),
    path("home",v1.home,name='home'),
    path("login/",v1.login,name='login'),
    path('home/todo',v2.todo,name='todo'),
    path('home/todo/addtask',v2.addtask,name='addtask'),
    path('home/todo/yourtask',v2.yourtask,name='yourtask'),
    path('del/<int:pk>',v2.remove,name="del"),
    path('profile/',v1.showdata,name='profile'),
    path('logout',v1.logout,name='logout'),
    path('adminlog',v3.admin,name='adminlog'),
    path('Teacherlogin',v3.teacherlogin,name='Teacherlogin'),
    path('teacherhome',v3.teacherhome,name='teacherhome'),
    path('tprofile',v3.tprofile,name='tprofile'),
    path('student',v3.student,name='student'),
    path('msg/<str:pk>',v3.contact,name='msg'),
    path('message',v1.message,name='message'),
    path('delete/<int:pk>',v3.remove,name="delete"),
    path('contenteng',v1.eng,name="contenteng"),
    path('contentsci',v1.sci,name="contentsci"),
    path('contentcomp',v1.comps,name="contentcomp"),
    path('contact/<str:pk>',v1.contact,name="contact"),
    path('englishs',v1.sub,name="englishs"),
    path('sciences',v1.scie,name="sciences"),
    path('addcontent',v4.addcontent,name="addcontent"),
    path('showcontent',v4.show,name="showcontent"),
    path('addquestion',v5.addqtn,name="addquestion"),
    path('addans/<int:pk>',v5.addans,name="addans"),
    path('qtnans',v5.qtnans,name="qtnans"),
    path('delqtn/<int:pk>',v5.delqtn,name='delqtn'),
    path('edit/<int:pk>',v5.edit,name="edit"),
    path('delt/<int:pk>',v5.delete,name="delt"),
    path('showqtn',v5.showqtn,name="showqtn"),
    path('computers',v1.comp,name="computers"),
    path('trycode/<int:pk>',v1.trycode,name="trycode"),
    path('quiz/<str:pk>',v6.welcome,name='quiz'),
    path('engquiz',v6.engquiz,name="engquiz"),
    path('sciquiz',v6.sciquiz,name="sciquiz"),
    path('compquiz',v6.compquiz,name="compquiz"),
    path('engresult',v6.engresult,name="engresult"),
    path('compresult',v6.compresult,name="compresult"),
    path('sciresult',v6.sciresult,name="sciresult"),
    path('engsaveans',v6.engsaveans,name="engsaveans"),
    path('compsaveans',v6.compsaveans,name="compsaveans"),
    path('scisaveans',v6.scisaveans,name="scisaveans"),
    path('score',v6.score,name="score"),
    path('msgs',v3.msg,name="msgs"),
    path('delte/<int:pk>',v3.delte,name="delte"),
    path('addquiz',v6.addquiz,name="addquiz"),
    path('search',v4.dict,name="search"),
    path('src',v4.search,name='src')

    
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
