# Generated by Django 2.1.5 on 2022-10-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20221013_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='art_meta_tags',
            field=models.TextField(blank=True, default='-', max_length=1000),
        ),
    ]
