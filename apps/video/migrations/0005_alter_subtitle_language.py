# Generated by Django 5.1.1 on 2024-09-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_remove_subtitle_end_time_remove_subtitle_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtitle',
            name='language',
            field=models.CharField(max_length=50, null='True'),
        ),
    ]
