# Generated by Django 3.0.4 on 2020-04-19 14:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_experience_include_in_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
