import dataclasses
from pickle import NONE
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import *
from .forms import *

# Create your views here.
def home(request):
    allMovies = Movie.objects.all()        
    print(allMovies)

    context = {
        "movies": allMovies,
    }

    return render(request, 'main/index.html', context)


# detail page
def detail(request, id):
    movie = Movie.objects.get(id=id) #select * from movie where id=id

    context = {
        "movie": movie
    }
    return render(request, 'main/details.html', context)

# add movies to the database
def add_movies(request):
    if request.method == "POST":
        form = MovieForm(request.POST or None)

        # check if form is valid
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:
         form = MovieForm()
    return render(request, 'main/addmovies.html', {"form": form})

def edit_movies(request, id):

    movie = Movie.objects.get(id=id)

    if request.method == "POST":
        form = MovieForm(request.POST or None, instance=movie)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:detail", id)

    else:
        form = MovieForm(instance=movie)
    return render(request, 'main/addmovies.html', {"form": form})

def delete_movies(request, id):

    movie = Movie.objects.get(id=id)

    movie.delete()
    return redirect("main:home")
    