# Generated by Django 3.1 on 2021-05-08 18:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0007_auto_20210508_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 23, 51, 46, 873988)),
        ),
    ]
