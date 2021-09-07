from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserDetail(models.Model):
    name = models.CharField(max_length=50,default="")
    time=models.DateTimeField(default=datetime.now)
    profile_img=models.ImageField(upload_to='images',default="images\default.png")
    notif= models.BooleanField(default=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE,default="")
    

    def __str__(self):
        return self.user.first_name

class Subjects(models.Model):
    subject=models.CharField(max_length=50)
    name = models.CharField(max_length=50,default="")
    username = models.CharField(max_length=50,default="")
    teacher =models.CharField(max_length=50,default="")
    subjectincharge=models.CharField(max_length=50,default="")
    message = models.TextField(default="")
    score= models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.username

    
