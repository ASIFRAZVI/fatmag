# Generated by Django 5.1.1 on 2024-09-08 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_alter_video_video_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtitle',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='subtitle',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='subtitle',
            name='content',
            field=models.FileField(upload_to='subtitles/'),
        ),
    ]
