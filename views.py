from django.shortcuts import render
from .models import HighScore

def game(request):
    # Get or create high score
    hs, created = HighScore.objects.get_or_create(id=1)
    return render(request, "game.html", {"highscore": hs.score})

def update_score(request):
    if request.method == "POST":
        new_score = int(request.POST.get("score"))
        hs, created = HighScore.objects.get_or_create(id=1)

        if new_score > hs.score:
            hs.score = new_score
            hs.save()

    return render(request, "score_saved.html")
