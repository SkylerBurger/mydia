# Generated by Django 2.2.7 on 2019-11-09 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0005_auto_20191107_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='book', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]