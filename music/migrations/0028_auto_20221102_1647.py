# Generated by Django 2.1.5 on 2022-11-02 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0027_songcomments_deleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songcomments',
            old_name='liked_date',
            new_name='commented_date',
        ),
        migrations.RenameField(
            model_name='songcomments',
            old_name='liked_song',
            new_name='commented_on_song',
        ),
        migrations.RenameField(
            model_name='songcomments',
            old_name='liked_user',
            new_name='commented_user',
        ),
    ]
