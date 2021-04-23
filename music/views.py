from django.contrib import messages
from django.db import transaction
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from music.forms import SignupForm, NewMusicForm
from music.models import Genre, Label, Music


def index(request):
    return render(request, "index.html")


class GenreCreate(generic.CreateView):
    model = Genre
    template_name = 'music/new-genre.html'
    fields = ("title",)
    success_url = '/'


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('index')
            else:
                return HttpResponse("Invalid username & password")

    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


class NewLabel(generic.CreateView):
    model = Label
    fields = ("label",)
    template_name = "music/new-label.html"
    context_object_name = "new-label"
    success_url = "/"


class MusicList(generic.ListView):
    model = Music
    template_name = "music/musics.html"
    context_object_name = "musics"


@transaction.atomic
@login_required
def new_music(request):

    if request.POST:
        form = NewMusicForm(request.POST, request.FILES or None)
    else:
        form = NewMusicForm()

    if form.is_valid():
        form_obj = form.save()
        messages.success(request, "Your music was successfully added. Happy MusicPey!")
        return redirect("music", form_obj.slug)

    params = {
        'form': form,
    }
    return render(request, "music/new-music.html", params)


@transaction.atomic
@login_required
def update_music(request, pk):

    form = get_object_or_404(Music, id=pk)
    params = {
        'form': form,
    }
    return render(request, "music/update-music.html", params)


class MusicDetail(generic.DetailView):
    model = Music
    template_name = "music/music.html"
    context_object_name = "music"
