from django.urls import path
from .views import DirectorList, DirectorDetail, MovieList, MovieDetail, ReviewList, ReviewDetail

urlpatterns = [
    path('api/v1/directors/', DirectorList.as_view(), name='director-list'),
    path('api/v1/directors/<int:pk>/', DirectorDetail.as_view(), name='director-detail'),
    path('api/v1/movies/', MovieList.as_view(), name='movie-list'),
    path('api/v1/movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    path('api/v1/reviews/', ReviewList.as_view(), name='review-list'),
    path('api/v1/reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
