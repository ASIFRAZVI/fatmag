# restframework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
import subprocess
from django.conf import settings

# models imports
from apps.video.models.video import Video, Subtitle

# thirdparty packages import
from drf_spectacular.utils import extend_schema

# serializers imports
from apps.video.serializers import VideoSerializer, GetVideoSerializer
from apps.base.serializers.base import UUIDFeildSerializer


# class to list, retrieve videos and add video
class VideoView(APIView):

    # Swagger Schema for post api
    @extend_schema(
        request=VideoSerializer,
        # responses=VideoSerializer,
        operation_id="add-video_1",
    )

    # create video obj and CC
    def post(self, request, *args, **kwargs):
        """function to add or create video it requires title,
        description and video-file and in background it will
        automatically process the subtitle and creates
        subtitle object and subtitle.srt file"""

        # Get form data
        data = request.data

        # handle Empty form or missing data
        if data is None:
            return Response(
                {"error": "No data provided, please enter required inputs"}, status=400
            )

        # serialize the form data
        serializer = VideoSerializer(data=data)

        # handle invalid serializer form data
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=400)

        # Save the serializer
        video = serializer.save()

        # Path to the uploaded video file
        video_path = video.video_file.path
        # print(video_path)

        # get the subtitle-dir from setting.py
        subtitle_dir = os.path.join(settings.MEDIA_ROOT)

        # defination of subtitle path or filename
        subtitle_filename = os.path.join("subtitles", f"video-subtitle-{video.id}.srt")

        # join both subtitle Dir & subtitle filename to get actual system subtitle file
        subtitle_path = os.path.join(subtitle_dir, subtitle_filename)

        # Extract subtitles using CCExtractor #commented bcz this package is not working properly
        # command = (
        #     [
        #         "package_dir\CCExtracror_tools\CCExtracror_tools\CCExtractor_win_portable\ccextractorwinfull.exe",
        #         video_path,
        #         "-o",
        #         subtitle_path,
        #     ]
        # )

        # try:
        # subprocess.run(command, check=True)
        # except subprocess.CalledProcessError as e:
        # return Response({"error": f"Failed to extract subtitles: {str(e)}"}, status=400)

        # Use FFmpeg to extract subtitles
        ffmpeg_path = os.path.join(
            settings.BASE_DIR.parent, "package_dir", "CCExtracror_tools", "CCExtracror_tools", "ffmpeg", "bin", "ffmpeg.exe"
        )

        command = [
            # "ffmpeg\bin\ffmpeg.exe",
            # package path
            ffmpeg_path,
            "-i",
            # video path
            video_path,
            "-map",
            "0:s:0",
            # subtitle path
            subtitle_path,
        ]

        # check any errors while extracting the CC
        try:
            # subprocess.run(command, check=True)
            subprocess.run(command, check=True)
        # except subprocess.CalledProcessError as e:
        except:
            # return Response({"error": f"Failed to extract subtitles: {str(e)}"}, status=400)
            return Response(
                {"error": "subtitle does not exists! please upload the proper video!"},
                status=400,
            )

        # Subtitle table input data
        subtitle_data = {"video": video, "language": "en", "content": subtitle_filename}

        # create subtile object and save which is associated with particular video
        try:
            subtitle_obj = Subtitle.objects.create(**subtitle_data)
            subtitle_obj.save()
        except Exception as e:
            return Response({"error": str(e)}, status=400)

        # after extracting CC Final success response
        return Response({"success": "video and subtitles are created"}, status=201)

    # Swagger schema to get apis
    @extend_schema(
        request=GetVideoSerializer,
        # responses=GetVideoSerializer,
        operation_id="get-video_1",
    )

    # list or retrieve videos and associated subtitles
    def get(self, request, pk=None, *args, **kwargs):
        """this method returns all video and its associated subtitles
        if the PK or ID not provided or None, If pk or ID provided then
        it will return particular video and its associated subtitles"""

        # handle if pk is None or not provided
        if pk is None:
            try:
                # return all videos
                videos = Video.objects.all()
            except:
                # Handle if DB is Empty
                return Response({"error": "no videos are available!"}, status=400)

            # serialize the DB data
            serializer = GetVideoSerializer(videos, many=True)
            # Final response with the filtered data
            return Response(serializer.data, status=200)

        # Handle is ID or PK is provided
        # serialize the input ID
        id_serializer = UUIDFeildSerializer(data={"id": pk})

        # Handle invalid input UUid
        if not id_serializer.is_valid():
            return Response({"error": "please enter valid uuid"}, status=400)

        # get particular Input id video and subtitle Data
        try:
            video = Video.objects.get(id=pk)
        except:
            return Response({"error": "entered uuid is not exists in db"}, status=400)

        # serialize the DB data
        serializer = GetVideoSerializer(video)
        # return the final success response with filtered clean data
        return Response(serializer.data, status=200)
