# Generated by Django 3.0.4 on 2020-03-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_date_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]
