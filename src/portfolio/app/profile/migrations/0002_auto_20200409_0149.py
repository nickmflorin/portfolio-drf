# Generated by Django 3.0.4 on 2020-04-09 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='intro',
            field=models.CharField(max_length=256),
        ),
    ]
