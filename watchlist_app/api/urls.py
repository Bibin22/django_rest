from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('stream_create', StreamPlatformVS, basename='stream_create')
urlpatterns = [
    # path("list/", movie_list, name="movie_list"),
    # path("list/<int:pk>/", movie_details, name='movie_detail'),
    path("list/", MovieListAPI.as_view(), name="list"),
    path("list/<str:pk>", MovieDetailAPI.as_view(), name='movie_detail'),
    path("watch_list/", WatchListAPI.as_view(), name='watch_list'),
    path("watch_lists/", WatchLists.as_view(), name='watch_lists'),
    path("watch_list/<str:id>", WatchListDetails.as_view(), name='watch_list_detail'),
    path("streaming_list/", StreamingPlatformList.as_view(), name='streaming_list'),
    path("streaming_list/<str:id>", StreamingPlatformDetails.as_view(), name='streaming_list_detail'),
    # path('review', ReviewList.as_view(),name='review'),
    # path('review_detail/<str:pk>', ReviewDetails.as_view(),name='review_detail')
    path('<str:pk>/review_create', ReviewCreate.as_view(),name='review_create'),
    path("<str:pk>/review", ReviewList.as_view(), name='review'),
    path("review/<str:pk>", ReviewDetails.as_view(), name='review_detail'),
    path('', include(router.urls)),

    path('reviews/', UserReview.as_view(), name='reviews')


]