# Generated by Django 2.2.6 on 2019-10-24 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20191019_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='form',
        ),
        migrations.RemoveField(
            model_name='book',
            name='platform',
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=200, verbose_name='platform')),
                ('form', models.CharField(max_length=200, verbose_name='format')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
    ]
