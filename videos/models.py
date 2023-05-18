from django.db import models
import uuid


class Video(models.Model):
    WATER_MARK_DEFAULT = "Good Work. Good People."
    STATUS_PENDING = "PENDING"
    STATUS_PROCESSING = "PROCESSING"
    STATUS_ERROR = "ERROR"
    STATUS_SUCCESS = "SUCCESS"
    STATUSES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PROCESSING, "Processing"),
        (STATUS_ERROR, "Error"),
        (STATUS_SUCCESS, "Success"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to="upload")
    water_mark = models.TextField(max_length=150, default=WATER_MARK_DEFAULT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_PENDING)
