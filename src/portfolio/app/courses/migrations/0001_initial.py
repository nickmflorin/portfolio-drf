# Generated by Django 3.0.4 on 2020-04-01 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(help_text='Name of the course or class.', max_length=64, unique=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='education.Education')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
