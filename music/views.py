from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from music.forms import SignupForm
from music.models import Genre


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
