from django.shortcuts import render
from django.http import HttpResponse
from . import getInfo

# Create your views here.

def accueil(request):
	return render(request, "ex00/accueil.html")

def make_grid(width, position):
    grid = []
    for y in range (0, width):
        new = []
        for x in range (0, width):
            if (x == position['x']) and (y == position['y']):
                new.append('O')
            else:
                new.append('X')
        grid.append(new)
    return grid

def worldmap(request):
	print("hey new game?")
	settings = getInfo.moviemon()
	settings.load_default_settings()
	width = settings.grid_size['width']
	position = settings.position
	return render(request, "ex00/worldmap.html", { 'grid':make_grid(width,position) })

def battle(request):
	return render(request, "ex00/battle.html")

def moviedex(request):
	return render(request, "ex00/moviedex.html")

def options(request):
	return render(request, "ex00/options.html")

def options_load_game(request):
	return render(request, "ex00/options_load_game.html")

def options_save_game(request):
	return render(request, "ex00/options_save_game.html")