# Generated by Django 2.1.5 on 2022-10-13 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_category_cat_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default=1665639387.9306552, max_length=50, unique=True),
        ),
    ]