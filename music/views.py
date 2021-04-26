from django.contrib import messages
from django.db import transaction
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from music.forms import SignupForm, MusicForm
from music.models import Genre, Label, Music
from django.urls import reverse_lazy, reverse


def index(request):
    return render(request, "index.html")


class GenreCreate(generic.CreateView):
    model = Genre
    fields = ("title",)
    success_url = '/'


class CreateLabel(generic.CreateView):
    model = Label
    fields = ("label",)
    success_url = "/"


class MusicList(generic.ListView):
    model = Music


@transaction.atomic
@login_required
def create_music(request):
    if request.POST:
        form = MusicForm(request.POST, request.FILES)
    else:
        form = MusicForm()

    if form.is_valid():
        form_obj = form.save()
        messages.success(request, "Your music was successfully added. Happy MusicPey!")
        return redirect("music", form_obj.slug)

    params = {
        'form': form,
    }
    return render(request, "music/new-music.html", params)


class UpdateMusic(generic.UpdateView):
    model = Music
    fields = ("title", "audio_file")
    success_url = reverse_lazy("musics")


def update_music(request, pk):
    music_object = get_object_or_404(Music, id=pk)
    form = MusicForm(request.POST or None, request.FILES or None, instance=music_object)
    params = {
        'form': form,
    }
    return render(request, "music/update-music.html", params)


class MusicDetail(generic.DetailView):
    model = Music


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
