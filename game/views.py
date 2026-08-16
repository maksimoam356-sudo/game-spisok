from django.shortcuts import render

from game.models import Game


# Create your views here.
def home(request):
    print("jokpfwlpfdkl")
    games = Game.objects.all()
    print(games)
    return render(request, 'gamenews.html', {'games': games})

def gamedetail(request, game_id):
    game = Game.objects.get(pk=game_id)
    return render(request, 'gamedetail.html', {'game': game})

