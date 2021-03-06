# Generated by Django 2.2.6 on 2019-10-19 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('season', models.FloatField(verbose_name='season')),
                ('release_year', models.CharField(max_length=5, verbose_name='release year')),
                ('platform', models.CharField(max_length=200, verbose_name='platform')),
                ('form', models.CharField(max_length=200, verbose_name='format')),
            ],
        ),
    ]
