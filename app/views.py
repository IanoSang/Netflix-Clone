from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.contrib.auth.models import User

TMDB_API_KEY = '700876f2ae61f5f3295a19fe9486cd55'


# Create your views here.
def Home(request):
    return render(request, 'index.html')


def movies(request):
    return render(request, 'movies.html')



def search(request):
    # Get the query from the search box
    query = request.GET.get('q')
    print(query)

    # If the query is not empty
    if query:

        # Get the results from the API

        data = requests.get(
            f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
        print(data.json())

    else:
        return render(request, 'movies.html')

    # Render the template
    return render(request, 'results.html', {
        "data": data.json(),
        "type": request.GET.get("type")
    })


def view_movies(request):
    data = requests.get(f"https://api.themoviedb.org/3/movie/297802?api_key={TMDB_API_KEY}&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/297802/recommendations?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, "movies.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "type": "movie",
    })


def view_series(request):
    data = requests.get(f"https://api.themoviedb.org/3/discover/tv?api_key={TMDB_API_KEY}&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/discover/tv?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, "series.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "type": "tv",
    })
