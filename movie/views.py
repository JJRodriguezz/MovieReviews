from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Movie

import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome to home Page</h1>')
    #return render(request, 'home.html')
    #return render(request, 'home.html', {'name': 'Juan Jose Rodriguez'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})

def about(request):
    #return HttpResponse('<h1>Welcome to About page</h1>')
    return render(request, 'about.html')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def statistics_view(request):
    matplotlib.use('Agg')
    # Obtener todas las películas
    all_movies = Movie.objects.all()

    # Crear un diccionario para almacenar la cantidad de películas por año
    movie_counts_by_year = {}

    # Filtrar las películas por año y contar la cantidad de películas por año
    for movie in all_movies:
        year = movie.year if movie.year else "None"
        if year in movie_counts_by_year:
            movie_counts_by_year[year] += 1
        else:
            movie_counts_by_year[year] = 1

    # Ancho de las barras
    bar_width = 0.5

    # Posiciones de las barras
    bar_positions = range(len(movie_counts_by_year))

    # Crear la gráfica de barras
    plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align='center')

    # Personalizar la gráfica
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)

    # Ajustar el espaciamiento entre las barras
    plt.subplots_adjust(bottom=0.3)

    # Guardar la gráfica en un objeto BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    #Convertir la gráfica a base64
    image_png = buffer.getvalue()
    buffer.close()
    graphic_years = base64.b64encode(image_png)
    graphic_years = graphic_years.decode('utf-8')

    # GRÁFICA 2: Cantidad de películas por género
    movie_counts_by_genre = {}
    for movie in all_movies:
        if movie.genre:  # Verificar que la película tenga género
            first_genre = movie.genre.split(',')[0].strip()  # Tomar solo el primer género
            movie_counts_by_genre[first_genre] = movie_counts_by_genre.get(first_genre, 0) + 1

    # Crear la segunda gráfica (Películas por género)
    plt.figure(figsize=(10, 5))
    plt.bar(movie_counts_by_genre.keys(), movie_counts_by_genre.values(), color='lightcoral')
    plt.title('Movies per Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar la imagen en Base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_png = buffer.getvalue()
    buffer.close()
    graphic_genres = base64.b64encode(image_png)
    graphic_genres = graphic_genres.decode('utf-8')
    plt.close()

    #Renderizar la plantilla statics.html con la gráfica
    return render(request, 'statistics.html', {'graphic':graphic_years, 'graphic_genres': graphic_genres})