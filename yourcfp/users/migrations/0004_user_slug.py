# Generated by Django 2.2 on 2019-06-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_organizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]