# Generated by Django 2.1.5 on 2022-10-13 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20221013_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]