# Generated by Django 3.1 on 2021-05-09 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20210509_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 18, 48, 13, 25868)),
        ),
    ]
