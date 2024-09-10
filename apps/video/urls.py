from django.urls import path
from apps.video.views.video import VideoView
from apps.video.views.subtitles import VideoSearchView


urlpatterns = [
    # add and get(all) video endpoint
    path("video/", VideoView.as_view(), name="upload-or-get-video"),
    # get video by video id path
    path("video/<uuid:pk>/", VideoView.as_view(), name="get-unique-video"),
    # search url it depends on video id and search query(timestamp)
    # note search query must be in the formate of 00:00:00
    path(
        "video/<uuid:pk>/search/<str:timestamp_query>/",
        VideoSearchView.as_view(),
        name="search-content",
    ),
]
