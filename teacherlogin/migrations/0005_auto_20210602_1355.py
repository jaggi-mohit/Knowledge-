# Generated by Django 3.1 on 2021-06-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherlogin', '0004_tmsg_notifs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tmsg',
            name='notifs',
        ),
        migrations.AddField(
            model_name='teacher',
            name='notifs',
            field=models.BooleanField(default=False),
        ),
    ]
