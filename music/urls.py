from django.urls import path

from music import views

urlpatterns = [
    path("", views.index, name="index"),

    path('signup/', views.signup, name="signup"),

    path("new/genre/", views.GenreCreate.as_view(), name="new-genre"),

    path("new/label/", views.NewLabel.as_view(), name="new-label"),

    path("all/", views.MusicList.as_view(), name="musics"),

    path("new/", views.new_music, name="new-music"),

    path("update/<int:pk>/", views.update_music, name="update-music"),

    path("open/<slug:slug>/", views.MusicDetail.as_view(), name="music"),

]