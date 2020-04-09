# Generated by Django 3.0.4 on 2020-04-09 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(blank=True, max_length=32, null=True)),
                ('comment', models.CharField(max_length=512)),
                ('public', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
