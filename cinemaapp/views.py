from django.http import HttpResponse
from django.shortcuts import render

from cinemaapp.forms import MovieForm

def form(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
    else:
        form = MovieForm()
    return render(request, "cinemaapp/form.html", {"form": form})
