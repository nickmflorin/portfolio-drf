# Generated by Django 3.0.4 on 2020-04-29 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0005_remove_optionality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='resume',
        ),
    ]
