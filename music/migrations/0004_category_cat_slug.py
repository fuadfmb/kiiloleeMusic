# Generated by Django 2.1.5 on 2022-10-13 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20221013_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default=datetime.datetime(2022, 10, 13, 8, 35, 43, 859121), max_length=50, unique=True),
        ),
    ]
