from django.shortcuts import render
from tmdb_api import query_movie, query_show, query_details_show, query_details_movie, get_movie_genre_dict, get_show_genre_dict
from django.contrib.auth.decorators import login_required
from onboarding.models import likedMovie, likedShow


# Create your views here.
@login_required()
def search_form(request):
    return render(request, "search-form.html")

@login_required()
def search_results(request):
    query = request.GET.get('query', '')
    media_type = request.GET.get('media-type', '')
    if media_type == 'movie':
        results = (query_movie(query))
    elif media_type == 'show':
        results = (query_show(query))
    else:
        results = {}
    return render(request, 'search-results.html', {'query': query, 'results': results, "media_type":media_type})

@login_required()
def search_item_details(request):
    media_id = request.GET.get('media-id', '')
    media_type = request.GET.get('media-type', '')
    if media_type == 'movie':
        is_liked = likedMovie.objects.filter(user=request.user, movieID=media_id).exists()
        results = (query_details_movie(media_id))
        movie_genres = get_movie_genre_dict()
        results['genre_names'] = [movie_genres[g['id']] for g in results['genres']]

    elif media_type == 'show':
        is_liked = likedShow.objects.filter(user=request.user, showID=media_id).exists()
        results = (query_details_show(media_id))
        show_genres = get_show_genre_dict()
        results['genre_names'] = [show_genres[g['id']] for g in results['genres']]
    else:
        results = {}
    return render(request, 'search-result-item-details.html', {'media_id': media_id, 'results': results, "media_type": media_type, "is_liked": is_liked})