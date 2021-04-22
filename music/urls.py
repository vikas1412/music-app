from django.urls import path

from music import views

urlpatterns = [
    path("", views.index, name="index"),

    path("new/genre/", views.GenreCreate.as_view(), name="new-genre"),

]