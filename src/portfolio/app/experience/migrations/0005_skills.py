# Generated by Django 3.0.4 on 2020-03-19 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
        ('experience', '0004_plural_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='skills',
            field=models.ManyToManyField(blank=True, help_text='Skilled worked on during employment.', related_name='experience_experience_skills', to='skills.Skill'),
        ),
    ]
