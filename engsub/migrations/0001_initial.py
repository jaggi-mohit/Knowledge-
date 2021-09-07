# Generated by Django 3.1 on 2021-05-17 09:36

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='english',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
