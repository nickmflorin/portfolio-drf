# Generated by Django 3.0.4 on 2020-03-25 00:19

from django.db import migrations, models
import portfolio.app.companies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=2)),
                ('logo', models.ImageField(null=True, upload_to=portfolio.app.companies.models.upload_to)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
    ]
