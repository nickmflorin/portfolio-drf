# Generated by Django 3.0.4 on 2020-04-19 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tagline',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]