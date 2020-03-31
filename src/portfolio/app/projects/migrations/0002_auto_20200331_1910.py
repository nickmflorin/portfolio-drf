# Generated by Django 3.0.4 on 2020-03-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='showcase',
            field=models.BooleanField(default=False, help_text='Determines whether or not the project will be showcased on the projects page.'),
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='name',
            field=models.CharField(help_text='Human readable name for the file that will be displayed to users in links to download/access the file.', max_length=64),
        ),
    ]
