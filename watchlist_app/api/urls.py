from django.urls import path
from .views import *
urlpatterns = [
    # path("list/", movie_list, name="movie_list"),
    # path("list/<int:pk>/", movie_details, name='movie_detail'),
    path("list/", MovieListAPI.as_view(), name="list"),
    path("list/<str:pk>", MovieDetailAPI.as_view(), name='movie_detail'),
    path("watch_list/", WatchListAPI.as_view(), name='watch_list'),
    path("watch_list/<str:id>", WatchListDetails.as_view(), name='watch_list_detail'),
    path("streaming_list/", StreamingPlatformList.as_view(), name='streaming_list'),
    path("streaming_list/<str:id>", StreamingPlatformDetails.as_view(), name='streaming_list_detail'),


]