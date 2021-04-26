from django.urls import path

from music import views

urlpatterns = [
    path("", views.index, name="index"),

    path('signup/', views.signup, name="signup"),

    path("new/genre/", views.GenreCreate.as_view(), name="create-genre"),

    path("new/label/", views.CreateLabel.as_view(), name="create-label"),

    path("all/", views.MusicList.as_view(), name="musics"),

    path("new/", views.create_music, name="create-music"),

    path("update/<int:pk>/", views.UpdateMusic.as_view(), name="update-music"),

    path("open/<slug:slug>/", views.MusicDetail.as_view(), name="music"),

]