# Generated by Django 3.1 on 2021-05-31 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0009_userdetail_notif'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
