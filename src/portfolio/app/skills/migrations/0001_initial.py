# Generated by Django 3.0.4 on 2020-03-27 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('experience', '0001_initial'),
        ('courses', '0001_initial'),
        ('projects', '0001_initial'),
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=64)),
                ('courses', models.ManyToManyField(blank=True, related_name='skills', to='courses.Course')),
                ('educations', models.ManyToManyField(blank=True, related_name='skills', to='education.Education')),
                ('experiences', models.ManyToManyField(blank=True, related_name='skills', to='experience.Experience')),
                ('projects', models.ManyToManyField(blank=True, related_name='skills', to='projects.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
