# Generated by Django 2.1.5 on 2022-10-13 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20221013_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='alb_about',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='alb_release_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
