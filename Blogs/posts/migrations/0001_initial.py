# Generated by Django 5.0.4 on 2024-04-19 00:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('content', models.CharField(max_length=10000000)),
            ],
        ),
    ]
