# Generated by Django 3.0.4 on 2020-03-30 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200330_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
