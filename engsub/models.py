from django.db import models

from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

class English(models.Model):
    title = models.CharField(max_length=100)
    video = EmbedVideoField(blank=True) 
    desc = models.TextField()

    def __str__(self):
        return self.title

class Science(models.Model):
    title = models.CharField(max_length=100)
    video = EmbedVideoField(blank=True) 
    desc = models.TextField()

    def __str__(self):
        return self.title

class Computer(models.Model):
    title = models.CharField(max_length=100)
    video = EmbedVideoField(blank=True)
    desc = RichTextField(blank=True,null=True)
    code = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.title

class show(models.Model):
    shws =RichTextField(blank=True,null=True)