from django.contrib import admin
from music.models import Music, Genre, Album, Band, Label


admin.site.register((Music, Genre, Album, Band, Label))
