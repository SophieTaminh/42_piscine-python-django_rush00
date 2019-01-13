from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import getInfo
import os

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
<<<<<<< Updated upstream
	from random import randint
	print(randint(0, 1))
	settings.saveTMP()
	return render(request, "ex00/worldmap.html", { 'grid':make_grid(width, height, position), 'found': 0 })
=======
	settings.saveTMP()

	test = settings.dump()
	print(test.position)
	return render(request, "ex00/worldmap.html", { 'grid':make_grid(width, height, position) })
>>>>>>> Stashed changes

def battle(request, id):
	print("battle!", id)
	settings = getInfo.moviemon()
	tmp = settings.dump()
	print(tmp.position)

	return render(request, "ex00/battle.html")

def moviedex(request):
	return render(request, "ex00/moviedex.html")

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

