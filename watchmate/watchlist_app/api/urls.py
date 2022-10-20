from django.urls import path
# from .views import movie_list, movie_details
from .views import WatchListAV, WatchDetailAV, StreamPlatformAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
]
