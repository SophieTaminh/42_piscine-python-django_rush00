from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import getInfo
import os
import random

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
	found_moviemon = ''
	if rand == 1:
		settings.nombreMovieballs += 1
	elif rand == 2:
		m = settings.get_random_movie(settings.moviemonListAvecDetail)
		found_moviemon = m['imdb_id']
	return rand, found_moviemon

def worldmap(request):
	move = request.GET.get('move', '')
	settings = getInfo.moviemon()
	settings = settings.dump()
	if do_move(settings, move):
		from random import randint
		settings.found, settings.found_moviemon = random_move_event(settings)
		print("found2!", settings.found_moviemon)
		settings.saveTMP()
		return(redirect("/worldmap"))
	width = settings.grid_size['width']
	height = settings.grid_size['height']
	position = settings.position
	return render(request, "ex00/worldmap.html", { 'grid':make_grid(width, height, position), 'found': settings.found, 'found_moviemon': settings.found_moviemon, 'numballs': settings.nombreMovieballs })

def battle(request, id):
	print("battle!", id)
	settings = getInfo.moviemon()
	game = settings.dump()
	game.nombreMovieballs
	moviemonABattre = game.get_movie(id)
	moviemonballTry = request.GET.get('movieball')
	message = ""
	forceJoueur = 0
	if (moviemonballTry):
		if (game.nombreMovieballs > 0):
			game.nombreMovieballs = game.nombreMovieballs - 1
			forceMonstre = float(moviemonABattre['rating']) * 10
			forceJoueur = game.get_strength()
			chance = 50 - int(forceMonstre) + forceJoueur * 5
			randomNumber = random.randint(1, 100)
			moviemonListAvecDetailClean = []
			if (chance >= randomNumber):
				game.moviedex.append(moviemonABattre)
				for moviemon in game.moviemonListAvecDetail:
					if (moviemon['title'] != moviemonABattre['nom']):
						moviemonListAvecDetailClean.append(moviemon)
				game.moviemonListAvecDetail = moviemonListAvecDetailClean
				game.saveTMP()
				message = "Tu as attrapé un moviemon !"
			else :
				message = "Retente ta chance !"
			game.saveTMP()
		else :
			message = "Tu n'as plus de movieballs"
	return render(request, "ex00/battle.html", {"message" : message, "forceJoueur" : forceJoueur, "nombreMovieballs" : game.nombreMovieballs, "moviemonABattre" : moviemonABattre, "id" : id})

def moviedex(request):
	settings = getInfo.moviemon()
	game = settings.dump()
	moviedex = game.moviedex
	return render(request, "ex00/moviedex.html", {"moviedex" : moviedex})

def moviedexDetail(request, id):
	settings = getInfo.moviemon()
	game = settings.dump()
	moviedex = game.moviedex
	return render(request, "ex00/moviedex_detail.html", {"moviemonDetail" : moviedex[int(id)]})

def options(request):
	return render(request, "ex00/options.html")

def options_load_game(request):
	print("load_game")
	settings = getInfo.moviemon()
	listeFichiers = os.listdir("saved_game/")
	listeGame = []
	for fichiers in listeFichiers:
		if (fichiers != "mypicklefile.txt"):
			listeGame.append(fichiers)
	selectionne = request.GET.get('selectionne')
	if (selectionne != None):
		for fichier in listeGame:
			if selectionne in fichier:
				game = settings.load(fichier)
				game.saveTMP()
				# return(redirect("/worldmap"))
	slota = False
	slotb = False
	slotc = False
	gameSplitA = 0
	gameSplitB = 0
	gameSplitC = 0
	for game in listeGame:
		if ("slota" in game):
			slota = True
			gameSplit = game.split("_")
			gameSplitA = gameSplit[1]
		if ("slotb" in game):
			slotb = True
			gameSplit = game.split("_")
			gameSplitB = gameSplit[1]
		if ("slotc" in game):
			slotc = True
			gameSplit = game.split("_")
			gameSplitC = gameSplit[1]
	return render(request, "ex00/options_load_game.html", { "slota" : slota, "slotb" : slotb, "slotc" : slotc, "slotaNiveau" : gameSplitA, "slotbNiveau" : gameSplitB, "slotcNiveau" : gameSplitC})

def options_save_game(request):
	print("save_game")
	settings = getInfo.moviemon()
	tmp = settings.dump()
	listeFichiers = os.listdir("saved_game/")
	listeGame = []
	for fichiers in listeFichiers:
		if (fichiers != "mypicklefile.txt"):
			listeGame.append(fichiers)
	print(listeGame)
	slota = False
	slotb = False
	slotc = False
	gameSplitA = 0
	gameSplitB = 0
	gameSplitC = 0
	for game in listeGame:
		if ("slota" in game):
			slota = True
			gameSplit = game.split("_")
			gameSplitA = gameSplit[1]
		if ("slotb" in game):
			slotb = True
			gameSplit = game.split("_")
			gameSplitB = gameSplit[1]
		if ("slotc" in game):
			slotc = True
			gameSplit = game.split("_")
			gameSplitC = gameSplit[1]
	nomSlot = request.GET.get('slot')
	NiveauMax = 10
	NiveauActuel = len(tmp.moviedex)
	if (nomSlot):
		saveName = "slot"+ nomSlot.lower() + "_" + str(NiveauActuel) + "_10.mmg"
		if ("slota" in saveName):
			commandeEffacer = os.system("rm -f saved_game/slota*")
			tmp.save(fileName = saveName)
		if ("slotb" in saveName):
			commandeEffacer = os.system("rm -f saved_game/slotb*")
			tmp.save(fileName = saveName)
		if ("slotc" in saveName):
			commandeEffacer = os.system("rm -f saved_game/slotc*")
			tmp.save(fileName = saveName)
	return render(request, "ex00/options_save_game.html", { "slota" : slota, "slotb" : slotb, "slotc" : slotc, "slotaNiveau" : gameSplitA, "slotbNiveau" : gameSplitB, "slotcNiveau" : gameSplitC})

def handler404(request):
    return render(request, '404.html', status=404)