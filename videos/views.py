from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import VideoUploadForm
from .models import Video
from .tasks import update_video_task
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def video_upload(request):
    if request.method == "POST":
        print(request.POST)
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            update_video_task.delay(video.id)
            return redirect("video_list")
    else:
        form = VideoUploadForm()
    return render(request, "video_upload.html", {"form": form})


def video_list(request):
    status_list = ["PENDING", "PROCESSING", "ERROR", "SUCCESS"]
    video_data = {}

    for status in status_list:
        video_data[status] = Video.objects.filter(status=status).values()

    return render(request, "video_list.html", {"video_data": video_data})
