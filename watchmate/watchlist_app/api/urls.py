from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import movie_list, movie_details
from .views import ReviewCreate, ReviewDetail, ReviewList, WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, StreamPlatformVS

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'), 
    
    path('', include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
        
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='streamplatform-create'),
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
