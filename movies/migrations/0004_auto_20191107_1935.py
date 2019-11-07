# Generated by Django 2.2.7 on 2019-11-07 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20191024_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecopy',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='copies', to='movies.Movie'),
        ),
    ]
