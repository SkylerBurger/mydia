# Generated by Django 2.2.6 on 2019-10-19 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.IntegerField(verbose_name='published'),
        ),
    ]
