from django.shortcuts import render
from django.views import generic

from music.models import Genre


def index(request):
    return render(request, "index.html")


class GenreCreate(generic.CreateView):
    model = Genre
    template_name = 'music/new-genre.html'
    fields = ("title",)
    success_url = '/'
