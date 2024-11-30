from django.db import models
from django.contrib.auth.models import User, AbstractUser
from tmdb_api import get_movie_genre_dict, get_show_genre_dict
# Create your models here.

class FavouriteGenres(models.Model):
    VIDEO_GENRE_CHOICES = (
        ("COMEDY", "Comedy"),
        ("DRAMA", "Drama"),
        ("HORROR", "Horror"),
        ("DOCUMENTRY", "Documentry"),
        ("MOCKUMENTRY", "Mockumentry"),
        ("THRILLER", "Thriller"),
    )
    MUSIC_GENRE_CHOICES = (
        ("ROCK", "Rock and Roll"),
        ("POP", "POP"),
        ("INDIE ROCK", "Indie/Alt Rock"),
        ("LOFI", "Lo-Fi"),
        ("RAP", "Rap"),
        ("BOOMBAP", "Boombap Rap"),
    )

    user = models.ForeignKey(User,verbose_name = 'User', on_delete=models.CASCADE)
    movieGenre = models.CharField(max_length=75,
                             choices=VIDEO_GENRE_CHOICES,
                             default="COMEDY")
    showGenre = models.CharField(max_length=75,
                                  choices=VIDEO_GENRE_CHOICES,
                                  default="MOCKUMENTRY")

    musicGenre = models.CharField(max_length=75,
                                  choices=MUSIC_GENRE_CHOICES,
                                  default="MOCKUMENTRY")

    def __str__(self):
        return (f'{self.musicGenre}, {self.movieGenre}, {self.showGenre}')

class likedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_movies")
    movieName = models.CharField(max_length=100)
    movieID = models.CharField(max_length=20)
    def __str__(self):
        return self.movieName

class likedShow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_shows")
    showName = models.CharField(max_length=100)
    showID = models.CharField(max_length=20)
    def __str__(self):
        return self.showName

class Profile(models.Model):
    VIDEO_GENRE_CHOICES = (
        ("COMEDY", "Comedy"),
        ("DRAMA", "Drama"),
        ("HORROR", "Horror"),
        ("DOCUMENTRY", "Documentry"),
        ("MOCKUMENTRY", "Mockumentry"),
        ("THRILLER", "Thriller"),
    )
    MUSIC_GENRE_CHOICES = (
        ("ROCK", "Rock and Roll"),
        ("POP", "POP"),
        ("INDIE ROCK", "Indie/Alt Rock"),
        ("LOFI", "Lo-Fi"),
        ("RAP", "Rap"),
        ("BOOMBAP", "Boombap Rap"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(verbose_name='bio', max_length=150, blank=True)
    photo = models.ImageField(default='profile_images/default-profile-picture.png', upload_to='profile_images')

    movieGenre = models.CharField(max_length=75,
                                  choices=VIDEO_GENRE_CHOICES,
                                  default="COMEDY")
    showGenre = models.CharField(max_length=75,
                                 choices=VIDEO_GENRE_CHOICES,
                                 default="MOCKUMENTRY")

    musicGenre = models.CharField(max_length=75,
                                  choices=MUSIC_GENRE_CHOICES,
                                  default="MOCKUMENTRY")

    def __str__(self):
        return self.user.username


