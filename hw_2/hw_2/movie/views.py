from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = list(Movie.objects.values())
    return render(request, 'listmovie.html', {'movies' : movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.filter(id=movie_id).values().first()
    return render(request, 'diteilsmovie.html', {'movie' : movie })

# Create your views here.
