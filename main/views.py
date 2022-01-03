from django.shortcuts import render, HttpResponse, redirect
from main.models import *
from .forms import MovieForm


def homepage(request):
    return render(request, "main/index.html")



def films(request):
    return render(request, "main/films.html")


def rating(request):
    return render(request, "main/rating.html")


def contact(request):
    return render(request, "main/contact.html")


def base(request):
    return render(request, "base.html")


def show(request):
    return render(request, "main/show.html")



def movies(request):
    movie_objects = Movie.objects.all()
    return render(request, 'main/films.html', {'movies': movie_objects})


def create_movie(request):
    if request.method == "POST":
       movie_form = MovieForm(request.POST)
       if movie_form.is_valid():
           movie_form.save()
           return redirect(movies)

    movie_form = MovieForm()
    return render(request, 'main/form.html', {'movie_form': movie_form})


def movie(request, id):
    try:
        movie_object = Movie.objects.get(id=id)
        return render(request, 'main/films.html', {'movie_object': movie_object})
    except Movie.DoesNotExist as e:
        return HttpResponse(f'Not found: {e}', status=404)

def edit_movie(request, id):
    movie_object = Movie.objects.get(id=id)

    if request.method == 'POST':
        movie_form = MovieForm(data=request.POST, instance=movie_object)
        if movie_form.is_valid():
            movie_form.save()
            return redirect(movie, id=id)
    movie_form = MovieForm(instance=movie_object)
    return render(request, 'main/form.html', {'movie_object': movie_object})

def delete_movie(request, id):
    movie_object = Movie.objects.get(id=id)
    movie_object.delete()
    return redirect(movies)


def news(request):
    return render(request, "main/news.html")


def kabar(request):
    return render(request, "main/kabar.html")

def news_2(request):
    return render(request, "main/news_2.html")   
