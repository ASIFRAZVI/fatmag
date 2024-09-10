# restframework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Django imports
import os

# models imports
from apps.video.models.video import Video


# class to search the subtiles
class VideoSearchView(APIView):
    def get(self, request, pk, timestamp_query=None, *args, **kwargs):
        """this method reponsible for searching subtitles based on particular
        video and timestamp note- timestamp must be in the formate of 00:00:00"""

        # Handle Empty timpstamp_query
        if timestamp_query is None:
            return Response({"error": "Please provide a timestamp query"}, status=400)

        # get the video based on provided video UUid or PK and handle if videos are not exists.
        try:
            video = Video.objects.get(id=pk)
        except:
            return Response({"error": "Video not found"}, status=400)

        # get the subtitle object from the video
        subtitle = video.subtitles.first()
        # print(subtitle)

        # HAndle if video not have subtitle object or it empty.
        if not subtitle:
            return Response({"error": "No subtitles found for the video"}, status=404)

        # get the subtile filepath from the subtitle obj
        subtitle_path = subtitle.content.path
        # print(subtitle_path)

        # Handle if subtitle path is empty
        if not os.path.exists(subtitle_path):
            return Response({"error": "Subtitle file not found"}, status=404)

        # read the lines of file
        with open(subtitle_path, "r") as file:
            lines = file.readlines()

        # initialize Empty result array
        search_results = []

        # define default timestap is None
        current_timestamp = None

        # itrate the lines
        for line in lines:
            # if --> in line
            if "-->" in line:
                # update curr_timestamp None to line and remove all white spaces
                current_timestamp = line.strip()

                # if search query exists in curr_timestamp then append that lines to search_results array
                if timestamp_query in current_timestamp:
                    search_results.append(
                        {
                            "timestamp": current_timestamp,
                            "text": lines[lines.index(line) + 1].strip(),
                        }
                    )

        # finally return the search_results with the ok status-code
        return Response(search_results, status=200)
