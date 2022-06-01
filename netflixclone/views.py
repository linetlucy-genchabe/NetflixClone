from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    # movies=Movie.objects.all()
    poster_url= "https://image.tmdb.org/t/p/w500/"
    response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=969509fb19ee305da27532300d83a5ae')
    movies_rosponse = response.json()
    # print(movies_rosponse)
    movies=movies_rosponse['results']
    # posters=movies.poster_path
    # posters=movies['poster_path']
    # print(movies)
    # poster=poster_url + posters
    return render(request, 'index.html',{'movies':movies,})
    # 'https://api.themoviedb.org/3/movie/popular?api_key=969509fb19ee305da27532300d83a5ae'