from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='home'),
    path("series/", views.view_series, name="series"),
    path("movies/", views.view_movies, name="movies"),
    path("search/", views.search, name="search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
