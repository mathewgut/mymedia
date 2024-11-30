from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path('join/', views.join, name='join'),
    path("profile/", views.profile, name='profile'),
    path("profile-edit/", views.profile_edit, name='profile-edit'),
    path("add-like-movie/", views.addFavouriteMovie, name='add-like-movie'),
    path("add-like-show/", views.addFavouriteShow, name='add-like-show')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)