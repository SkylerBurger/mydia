# Generated by Django 2.2.6 on 2019-10-24 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20191024_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviecopy',
            old_name='film',
            new_name='movie',
        ),
    ]
