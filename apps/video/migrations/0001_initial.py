# Generated by Django 5.1.1 on 2024-09-07 14:45

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('video_file', models.FileField(null=True, upload_to='videos/')),
            ],
            options={
                'db_table': 'video_master',
            },
        ),
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.video')),
            ],
            options={
                'db_table': 'subtitle_master',
            },
        ),
    ]
