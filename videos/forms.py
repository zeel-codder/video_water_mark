from django import forms
from .models import Video


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["video", "water_mark"]
        widgets = {
            "video": forms.FileInput(
                attrs={
                    "label": "Video",
                    "accept":"video/*"
                }
            ),
            "water_mark": forms.TextInput(
                attrs={
                    "placeholder": "Enter water mark",
                    "label": "Water mark",
                }
            ),
        }
