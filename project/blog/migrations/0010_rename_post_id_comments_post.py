# Generated by Django 3.2.10 on 2022-01-03 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20220103_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='post_id',
            new_name='post',
        ),
    ]