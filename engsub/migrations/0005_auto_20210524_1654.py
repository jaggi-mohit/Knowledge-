# Generated by Django 3.1 on 2021-05-24 11:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engsub', '0004_computer_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='code',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
