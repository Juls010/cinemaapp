from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from cinemaapp.forms import MovieForm
from cinemaapp.models import Movie

def form(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
    else:
        form = MovieForm()
    return render(request, "cinemaapp/form.html", {"form": form})



def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance = movie)
        if form.is_valid():
            form.save()
            return HttpResponse("Modificado")
        else:
            form = MovieForm(instance=movie)
        return render(request, "cinemaapp/form.html", {"form": form})
    

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "cinemaapp/list.html", {"movies": movies})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method =="POST":
        movie.delete()
        return redirect('movie_list')
    return render(request, "cinemaapp/confirm_delete.html", {})