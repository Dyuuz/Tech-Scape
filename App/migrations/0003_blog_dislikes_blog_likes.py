# Generated by Django 5.0.7 on 2024-10-11 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]