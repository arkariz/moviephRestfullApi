from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('refresh_movie/', RefreshMovieList.as_view()),
    path('newest_movie/', GetNewestMovie.as_view()),
    path('thumbnail_movie/', GetThumbnailMovie.as_view()),
    path('token/', GetToken.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)