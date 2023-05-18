# Create your tasks here

from .models import Video
from django.conf import settings
from celery import shared_task
import os
import ffmpeg


@shared_task
def update_video_task(video_id):
    video = Video.objects.get(id=video_id)
    try:
        video.status = "PROCESSING"
        video.save()
        video.video.name = add_text_watermark(video.video, video.water_mark)
        video.status = "SUCCESS"
        video.save()
    except Exception as e:
        print(e)
        video.status = "ERROR"
        video.save()


def add_text_watermark(video, water_mark):
    
    initial_path = os.path.join(settings.MEDIA_ROOT, video.name)
    file_name = video.name.split("/")
    file_name = file_name[-1]
    new_path = os.path.join(settings.MEDIA_ROOT, "output/" + file_name)
    
    ffmpeg.input(initial_path).output(
        new_path,
        vf=f"drawtext=text='{water_mark}':fontsize=30:fontcolor=white",
    ).run(overwrite_output=True)

    return "output/" + file_name
