# Generated by Django 3.0.4 on 2020-03-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_plural_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='gpa',
            field=models.FloatField(null=True),
        ),
    ]
