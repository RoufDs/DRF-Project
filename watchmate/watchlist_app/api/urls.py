from django.urls import path
# from .views import movie_list, movie_details
from .views import MovieListAView, MovieDetailAV

urlpatterns = [
    path('list/', MovieListAView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),
]
