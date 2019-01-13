from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path(r'^$', views.accueil, name='accueil'),
    path('worldmap', views.worldmap, name='worldmap'),
    path('battle/<slug:id>', views.battle, name='battle'),
    path('moviedex', views.moviedex, name='moviedex'),
    path('moviedex/<slug:id>', views.moviedex, name='moviedex'),
    path('options', views.options, name='options'),
    path('options/load_game', views.options_load_game, name='optionsLoad'),
    path('options/save_game', views.options_save_game, name='optionsSave'),
]
