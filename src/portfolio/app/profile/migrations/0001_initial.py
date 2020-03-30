# Generated by Django 3.0.4 on 2020-03-30 17:45

from django.db import migrations, models
import portfolio.app.profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('first_name', models.CharField(max_length=24)),
                ('last_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(max_length=24)),
                ('email', models.EmailField(max_length=24)),
                ('github_url', models.URLField(max_length=100)),
                ('linkedin_url', models.URLField(max_length=100)),
                ('resume', models.FileField(null=True, upload_to=portfolio.app.profile.models.upload_to)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
