from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def accueil(request):
	return render(request, "ex00/accueil.html")

def worldmap(request):
	return render(request, "ex00/worldmap.html")

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