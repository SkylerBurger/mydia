# Generated by Django 2.2.6 on 2019-10-17 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('release_year', models.IntegerField(verbose_name='release year')),
                ('mpaa_rating', models.CharField(max_length=5, verbose_name='MPAA rating')),
                ('run_time', models.IntegerField(verbose_name='run time')),
                ('platform', models.CharField(max_length=200, verbose_name='platform')),
                ('form', models.CharField(max_length=200, verbose_name='format')),
            ],
        ),
    ]
