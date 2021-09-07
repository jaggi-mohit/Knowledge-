from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Todo(models.Model):
    tasktitle= models.CharField(max_length=30)
    taskdesc= models.TextField()
    time=models.DateTimeField(default=datetime.now)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.tasktitle
    