from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movies


def index(request):
    movies = Movies.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})
    #output = ', '.join([m.title for m in movies])

    #Movies.objects.filter(release_year=19980)
    #Movies.objects.get(id=1)
    #return HttpResponse(output)


def detail(request, movie_id):
    movies = get_object_or_404(Movies, pk=movie_id)
    return render(request, 'movies/detail.html', {'movies': movies})
    # try:
    #     movies = Movies.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', {'movies': movies})
    # except Movies.DoesNotExist:
    #     raise Http404()