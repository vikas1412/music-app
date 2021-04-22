from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Genre(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def clean(self):

        genres = ["Rock", "Pop music", "Hip hop music", "Jazz", "Folk music", "Blues", "Popular music", "Heavy metal", "Country music", "Classical music", "Rhythm and blues", "Electronic dance music", "Electronic music", "Soul music", "Dance music", "Disco", "Techno", "Trance music", "Indie rock", "Alternative rock", "Instrumental", "Singing", "Dubstep", "Ambient music", "Pop rock",
 "Afrobeat", "African hip hop", "African heavy metal", "Benga", "Boomba", "Bongo Flava", "Fuji", "Highlife", "Hiplife",
        ]

        errors = {}
        title = self.title
        if title not in genres:
            errors['title'] = _(f"Must be one of genre from {genres}")
        if errors:
            raise ValidationError(errors)


def new_music_image_save(instance, filename):
    return 'images/{0}/{1}'.format(instance.title, filename)


def new_music_save(instance, filename):
    return 'music/{0}/{1}'.format(instance.title, filename)


class Album(models.Model):
    music = models.ForeignKey("Music", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    band = models.ForeignKey("Band", on_delete=models.SET_NULL, null=True)
    label = models.ForeignKey("Label", on_delete=models.SET_NULL, null=True)
    asin = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to=new_music_image_save, null=True, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.title


class Music(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    audio_file = models.FileField(upload_to=new_music_save, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class Band(models.Model):
    band = models.CharField(max_length=300, null=True, blank=True)
    music = models.ManyToManyField("Music", blank=True)

    def __str__(self):
        return self.band


class Label(models.Model):
    label = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.label


