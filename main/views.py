from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from main.models import *
from .forms import MovieForm, MessageForm, SearchForm
from django.views.generic import TemplateView, ListView, View
from django.db.models import Q
from django.contrib import messages



def homepage(request):
    return render(request, "main/index.html")



def films(request):
    return render(request, "main/films.html")


def rating(request):
    return render(request, "main/rating.html")


def contact(request):
    submitted = False
    if request.method == "POST":
       message_form = MessageForm(request.POST)
       if message_form.is_valid():
            message_form.save()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        message_form = MessageForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "main/contact.html", {'message_form': message_form, 'submitted': submitted})


def base(request):
    return render(request, "base.html")


def show(request):
    return render(request, "main/show.html")



def movies(request):
    movie_objects = Movie.objects.all()
    return render(request, 'main/index.html', {'movies': movie_objects})


# def create_movie(request):
#     if request.method == "POST":
#        movie_form = MovieForm(request.POST)
#        if movie_form.is_valid():
#            movie_form.save()
#            return redirect(movies)

#     movie_form = MovieForm()
#     return render(request, 'main/form.html', {'movie_form': movie_form})


# def movie(request, id):
#     try:
#         movie_object = Movie.objects.get(id=id)
#         return render(request, 'main/films.html', {'movie_object': movie_object})
#     except Movie.DoesNotExist as e:
#         return HttpResponse(f'Not found: {e}', status=404)

# def edit_movie(request, id):
#     movie_object = Movie.objects.get(id=id)

#     if request.method == 'POST':
#         movie_form = MovieForm(data=request.POST, instance=movie_object)
#         if movie_form.is_valid():
#             movie_form.save()
#             return redirect(movie, id=id)
#     movie_form = MovieForm(instance=movie_object)
#     return render(request, 'main/form.html', {'movie_object': movie_object})

# def delete_movie(request, id):
#     movie_object = Movie.objects.get(id=id)
#     movie_object.delete()
#     return redirect(movies)


def news(request):
    return render(request, "main/news.html")


def kabar(request):
    return render(request, "main/kabar.html")

def news_2(request):
    return render(request, "main/news_2.html")   




class Search(ListView):
    model = Movie
    template_name = "search_field.html"


    def get_queryset(self): 
        return Movie.objects.filter(
            Q(name__icontains= 'q')
        )
            


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        movies = Movie.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
        return render(request, 'main/search_field.html',
            {'movies': movies, 'query': q})
    else:
        return HttpResponse('Такого фильма нет.')



    #Сообщение
def message(request):
    if request.method == "GET":
        message_form = MessageForm(request.GET)
        if message_form.is_valid():
            message_form.save()
            return redirect(message)

    message_form = MessageForm()
    return render(request, 'main/message.html', {'message_form': message_form})



    
# def message(request):
#     if request.method == "GET":
#         message_form = MessageForm(request.GET)
#         message_form.is_favorite = True
#         message_form.save()
#         return render(request, 'main/message.html', {'message_form': message_form})



# def get_message(request, id):
#     letter = Message.objects.get(id=id)
#     letter.is_favorite = True
#     letter.save()
#     return render(request, 'main/message.html', {'letter': letter})

    
# def get(request, id):
#     if request.method == "GET":
#         letter = Message.objects.get(id=id)
#         return render(request, 'main/message.html', {'get': letter})

class DialogsViews(View):
    model = Message
    template_name = "message.html"

    def get(self, request):
        message = Message.objects.get(id=id)
        return render(request, 'main/message.html', {'get': message})
