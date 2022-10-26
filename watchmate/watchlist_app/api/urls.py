from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import movie_list, movie_details
from .views import (
                        ReviewCreate,
                        ReviewDetail,
                        ReviewList,
                        WatchListAV,
                        WatchDetailAV,
                        StreamPlatformAV,
                        StreamPlatformDetailAV,
                        StreamPlatformVS,
                        UserReview,
                        WatchList
                    )

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'), 
    path('list2/', WatchList.as_view(), name='watch-list'), 
    
    path('', include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
        
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='streamplatform-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
    path('reviews/', UserReview.as_view(), name='user-review-detail'),
]
