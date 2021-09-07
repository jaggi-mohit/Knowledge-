from django.db import models

# Create your models here.
class showdata(models.Model):
    question=models.TextField()
    
    username=models.CharField(max_length=50,default="")

    
    def __str__(self):
        return self.username


class ans(models.Model):
    answers= models.TextField()
    username=models.CharField(max_length=50,default="")
    qtn = models.ForeignKey(showdata,on_delete=models.CASCADE,default="")
    

    def __str__(self):
        return self.qtn.username