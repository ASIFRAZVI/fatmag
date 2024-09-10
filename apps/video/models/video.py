from django.db import models
from apps.base.models.base import BaseModel


# video schema
class Video(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to="videos/", null=False)

    class Meta:
        db_table = "video_master"


# subtitle schema
class Subtitle(BaseModel):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="subtitles")
    language = models.CharField(max_length=50, null="True")
    content = models.FileField(upload_to="subtitles/")

    class Meta:
        db_table = "subtitle_master"
