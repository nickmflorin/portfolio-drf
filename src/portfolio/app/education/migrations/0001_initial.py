# Generated by Django 3.0.4 on 2020-03-25 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '__first__'),
        ('schools', '__first__'),
        ('projects', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('start_month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('start_year', models.IntegerField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)])),
                ('end_month', models.IntegerField(blank=True, choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True)),
                ('end_year', models.IntegerField(blank=True, choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], null=True)),
                ('current', models.BooleanField(default=False)),
                ('degree', models.CharField(max_length=64)),
                ('major', models.CharField(max_length=64)),
                ('minor', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('concentration', models.CharField(blank=True, max_length=64, null=True)),
                ('gpa', models.FloatField(null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('projects', models.ManyToManyField(blank=True, help_text='Projects worked on during education.', related_name='education_education_projects', to='projects.Project')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.School')),
                ('skills', models.ManyToManyField(blank=True, help_text='Skilled worked on during education.', related_name='education_education_skills', to='skills.Skill')),
            ],
            options={
                'verbose_name_plural': 'Education History',
            },
        ),
    ]
