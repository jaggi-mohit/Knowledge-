# Generated by Django 3.1 on 2021-05-31 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compquiz',
            name='Sub',
        ),
        migrations.RemoveField(
            model_name='compquiz',
            name='username',
        ),
        migrations.RemoveField(
            model_name='engquiz',
            name='Sub',
        ),
        migrations.RemoveField(
            model_name='engquiz',
            name='username',
        ),
        migrations.RemoveField(
            model_name='sciquiz',
            name='Sub',
        ),
        migrations.RemoveField(
            model_name='sciquiz',
            name='username',
        ),
    ]
