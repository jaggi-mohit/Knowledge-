
from django.db.models.deletion import CASCADE

from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    subject= models.CharField(max_length=50)
    qualification =models.CharField(max_length=50)
    profile_img=models.ImageField(upload_to='images',default="images\default.png")
    isteacher = models.BooleanField(default=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE,default="")
    notifs= models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class Tmsg(models.Model):
    
    Fromuser= models.CharField(max_length=50)
    msg=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
