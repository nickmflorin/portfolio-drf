# Generated by Django 3.0.4 on 2020-03-25 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '0002_auto_20200325_1354'),
        ('companies', '0001_initial'),
        ('projects', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('current', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('projects', models.ManyToManyField(blank=True, help_text='Projects worked on during employment.', related_name='experience_experience_projects', to='projects.Project')),
                ('skills', models.ManyToManyField(blank=True, help_text='Skilled worked on during employment.', related_name='experience_experience_skills', to='skills.Skill')),
            ],
            options={
                'verbose_name_plural': 'Experience History',
            },
        ),
    ]
