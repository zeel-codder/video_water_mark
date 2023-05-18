# Generated by Django 4.2.1 on 2023-05-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0002_rename_videos_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="water_mark",
            field=models.TextField(default="Good Work. Good People.", max_length=150),
        ),
        migrations.AlterField(
            model_name="video",
            name="video",
            field=models.FileField(upload_to="static"),
        ),
    ]
