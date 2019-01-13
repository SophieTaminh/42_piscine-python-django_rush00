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

def do_move(settings, move):
	did_move = False
	width = settings.grid_size['width']
	height = settings.grid_size['height']
	position = settings.position
	if (move=='left'):
		if position['x'] > 0:
			settings.position['x'] = position['x'] - 1
			did_move = True
		return(redirect("/worldmap"))
	if (move=='right'):
		if position['x'] < width - 1:
			settings.position['x'] = position['x'] + 1
			did_move = True
		return(redirect("/worldmap"))
	if (move=='up'):
		if position['y'] > 0:
			settings.position['y'] = position['y'] - 1
			did_move = True
	if (move=='down'):
		if position['y'] < height - 1:
			settings.position['y'] = position['y'] + 1
			did_move = True
	return did_move

def random_move_event(settings):
	from random import randint
	rand = randint(0, 2)
	if rand == 1:
		settings.nombreMovieballs += 1
	elif rand == 2:
		junk = 0 # TODO: found a Moviemon
	return rand

def worldmap(request):
	move = request.GET.get('move', '')
	settings = getInfo.moviemon()
	settings = settings.dump()
	if do_move(settings, move):
		from random import randint
		settings.found = random_move_event(settings)
		settings.saveTMP()
		return(redirect("/worldmap"))
	width = settings.grid_size['width']
	height = settings.grid_size['height']
	position = settings.position
	return render(request, "ex00/worldmap.html", { 'grid':make_grid(width, height, position), 'found': settings.found, 'numballs': settings.nombreMovieballs })

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
