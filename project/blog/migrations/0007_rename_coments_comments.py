# Generated by Django 3.2.10 on 2022-01-01 20:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_coments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coments',
            new_name='Comments',
        ),
    ]
