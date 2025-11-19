
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to the Bee Game!")

def game_view(request):
    return render(request, 'bee_game/game.html')
