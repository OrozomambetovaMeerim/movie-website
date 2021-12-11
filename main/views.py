from django.shortcuts import render, HttpResponse, redirect
from main.models import *


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