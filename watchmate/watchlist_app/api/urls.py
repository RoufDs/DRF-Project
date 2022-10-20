from django.urls import path
# from .views import movie_list, movie_details
from .views import ReviewDetail, ReviewList, WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),    
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
        
    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
    # path('stream/1/review/', ReviewList.as_view(), name='streamplatform-detail'),
    # path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail')
]
