# Generated by Django 3.1 on 2021-05-16 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science', '0005_auto_20210516_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
