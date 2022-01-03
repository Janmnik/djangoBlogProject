# Generated by Django 3.2.10 on 2022-01-03 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comments_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]