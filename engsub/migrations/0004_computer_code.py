# Generated by Django 3.1 on 2021-05-24 11:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engsub', '0003_computer_science'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='code',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]