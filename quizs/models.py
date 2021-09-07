from django.db import models

# Create your models here.

from django.db import models

class EngQuiz(models.Model):
    question=models.CharField(max_length=100)

    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    
    
    

    answer = models.CharField(max_length=100)


class SciQuiz(models.Model):
    question=models.CharField(max_length=100)

    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    
    
    answer = models.CharField(max_length=100)



class CompQuiz(models.Model):
    question=models.CharField(max_length=100)

    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    
    
    answer = models.CharField(max_length=100)






