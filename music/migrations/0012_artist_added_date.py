# Generated by Django 2.1.5 on 2022-10-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20221019_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='added_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
