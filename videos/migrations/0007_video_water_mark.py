# Generated by Django 4.2.1 on 2023-05-18 03:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0006_remove_video_water_mark"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="water_mark",
            field=models.TextField(default="Good Work. Good People.", max_length=150),
        ),
    ]
