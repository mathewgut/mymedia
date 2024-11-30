from django.contrib import admin
from .models import FavouriteGenres, Profile, likedMovie, likedShow

# Register your models here.

admin.site.register(FavouriteGenres)
admin.site.register(Profile)
admin.site.register(likedMovie)
admin.site.register(likedShow)