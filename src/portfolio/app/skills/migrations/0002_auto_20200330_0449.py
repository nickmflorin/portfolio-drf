# Generated by Django 3.0.4 on 2020-03-30 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
