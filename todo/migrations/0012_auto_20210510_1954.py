# Generated by Django 3.1 on 2021-05-10 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20210510_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
