from django.urls import path
from .views import DirectorList, DirectorDetail, MovieList, MovieDetail, ReviewList, ReviewDetail, MovieReviewsList, DirectorsWithMoviesCount

urlpatterns = [
    path('directors/', DirectorList.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorDetail.as_view(), name='director-detail'),
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('movies/<int:movie_id>/reviews/', MovieReviewsList.as_view(), name='movie-reviews-list'),
    path('directors/<int:pk>/', DirectorsWithMoviesCount.as_view(), name='directors-with-movies-count'),
]

