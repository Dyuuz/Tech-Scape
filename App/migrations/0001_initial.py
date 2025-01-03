# Generated by Django 5.0.7 on 2024-07-31 03:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('username', models.CharField(default='anon', max_length=20, null=True)),
                ('body', models.TextField()),
                ('slug', models.SlugField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default='test.jpg', upload_to='')),
                ('dp', models.ImageField(blank=True, default='test.jpg', upload_to='')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.category')),
            ],
        ),
    ]
