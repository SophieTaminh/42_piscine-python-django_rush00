from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import getInfo

# Create your views here.

def accueil(request):
	settings = getInfo.moviemon()
	settings.load_default_settings()
	settings.saveTMP()
	return render(request, "ex00/accueil.html")

def make_grid(width, height, position):
    grid = []
    for y in range (0, height):
        new = []
        for x in range (0, width):
            if (x == position['x']) and (y == position['y']):
                new.append('O')
            else:
                new.append('X')
        grid.append(new)
    return grid

def displayObject(o):
	#print(str(o.__class__) + ": " + str(o.__dict__))
	print(o.position)

def worldmap(request):
	print("hey new game?")
	move = request.GET.get('move', '')
	settings = getInfo.moviemon()
	settings = settings.dump()
	print("settings.position")
	print(settings.position)
	displayObject(settings)
	width = settings.grid_size['width']
	height = settings.grid_size['height']
	position = settings.position
	if (move=='left'):
		if position['x'] > 0:
			settings.position['x'] = position['x'] - 1
			settings.saveTMP()
		return(redirect("/worldmap"))
	if (move=='right'):
		if position['x'] < width - 1:
			settings.position['x'] = position['x'] + 1
			settings.saveTMP()
		return(redirect("/worldmap"))
	if (move=='up'):
		if position['y'] > 0:
			settings.position['y'] = position['y'] - 1
			settings.saveTMP()
		return(redirect("/worldmap"))
	if (move=='down'):
		if position['y'] < height - 1:
			settings.position['y'] = position['y'] + 1
			settings.saveTMP()
		return(redirect("/worldmap"))
	from random import randint
	print(randint(0, 1))
	settings.saveTMP()
	return render(request, "ex00/worldmap.html", { 'grid':make_grid(width, height, position), 'found': 0 })

def battle(request, id):
	print("battle!", id)
	return render(request, "ex00/battle.html")

def moviedex(request):
	return render(request, "ex00/moviedex.html")

def options(request):
	return render(request, "ex00/options.html")

def options_load_game(request):
	return render(request, "ex00/options_load_game.html")

def options_save_game(request):
	return render(request, "ex00/options_save_game.html")
