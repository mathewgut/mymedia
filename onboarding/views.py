from django.shortcuts import render
from .models import FavouriteGenres, likedMovie, likedShow
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserCreationForm
from tmdb_api import request_popular_movies, request_popular_shows, request_high_rating_movies,request_high_rating_shows
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def join(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/join.html', {'form':form})

def index(request):
    if request.user.is_authenticated:
        return render(request, "index-authenticated.html",
                      {'request_popular_movies':request_popular_movies,'request_popular_shows':request_popular_shows,
                       'request_high_rating_movies':request_high_rating_movies, 'request_high_rating_shows':request_high_rating_shows})
    else:
        return render(request, "index.html", {'media-type':''})

@login_required
def user_logout(request):
    logout(request)
    return render(request, "registration/logged_out.html")

def join(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/join.html', {'form':form})

@login_required
def profile(request):
    liked_movies = likedMovie.objects.filter(user=request.user)
    liked_shows = likedShow.objects.filter(user=request.user)
    all_fav_genres = FavouriteGenres.objects.filter(user=request.user)
    return render(request, "profile.html", {'all_fav_genres':all_fav_genres, 'profile':profile, 'liked_movies':liked_movies, 'liked_shows':liked_shows})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to="profile")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile-edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def addFavouriteMovie(request):
    if request.method == 'POST':
        media_type = request.POST.get('media_type', '')
        movie_id = request.POST.get('movie_id', '')
        movie_name = request.POST.get('movie_name', '')

        is_liked = likedMovie.objects.filter(user=request.user, movieID=movie_id).exists()
        if is_liked:
            likedMovie.objects.filter(user=request.user, movieID=movie_id).delete()
            return redirect(f'/results/item/?media-id={movie_id}&media-type={media_type}')
        if media_type == 'movie' and movie_id and movie_name:
            liked_movie, created = likedMovie.objects.get_or_create(
                user=request.user,
                movieID=movie_id,
                defaults={'movieName': movie_name}
            )
        return redirect(f'/results/item/?media-id={movie_id}&media-type={media_type}')
    return redirect('index')

@login_required
def addFavouriteShow(request):
    if request.method == 'POST':
        media_type = request.POST.get('media_type', '')
        show_id = request.POST.get('show_id', '')
        show_name = request.POST.get('show_name', '')

        is_liked = likedShow.objects.filter(user=request.user, showID=show_id).exists()
        if is_liked:
            likedShow.objects.filter(user=request.user, showID=show_id).delete()
            return redirect(f'/results/item/?media-id={show_id}&media-type={media_type}')
        # Validate the inputs
        if media_type == 'show' and show_id and show_name:
            liked_show, created = likedShow.objects.get_or_create(
                user=request.user,
                showID=show_id,
                defaults={'showName': show_name}
            )
        return redirect(f'/results/item/?media-id={show_id}&media-type={media_type}')
    return redirect('index')