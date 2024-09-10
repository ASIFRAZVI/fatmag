from rest_framework import serializers
from apps.video.models.video import Video, Subtitle


#  video serializer for post request
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["title", "description", "video_file"]


# subtitle serializer
class SubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtitle
        fields = ["language", "content"]


#  nested serializer for list video
class GetVideoSerializer(serializers.ModelSerializer):
    subtitles = SubtitleSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ["id", "title", "description", "video_file", "subtitles"]
