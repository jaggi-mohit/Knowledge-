# Generated by Django 3.1 on 2021-05-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0004_userdetail_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='subjects',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]