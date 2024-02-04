import random
from django.shortcuts import render
from .models import Game

def roll_dice():
    return random.randint(1, 6)

def play_game(points_to_win):
    points = 0
    rolls = 0
    while True:
        roll = roll_dice()
        points += roll
        rolls += 1
        if points >= points_to_win:
            return points, rolls
        answer = input(f"You rolled a {roll}. Your total is {points}. Do you want to roll again? (y/n) ")
        if answer.lower() != 'y':
            return points, rolls

def load_top_games(points_to_win):
    top_games = Game.objects.filter(points__lte=points_to_win).order_by('-points')[:5]
    return top_games

def save_top_games(top_games, points_to_win):
    for game in top_games:
        game.save()

def display_top_games(top_games):
    return {'top_games': top_games}

def main(request):
    player_name = request.POST.get('player_name', '')
    points_to_win = int(request.POST.get('points_to_win', 0))
    again = request.POST.get('again', '')
    if again.lower() == 'y':
        points, rolls = play_game(points_to_win)
        if points < points_to_win:
            game = Game(player=player_name, points=points, rolls=rolls)
            game.save()
            top_games = load_top_games(points_to_win)
            return render(request, 'dice_game_app/index.html', {'top_games': top_games})
        elif points > points_to_win:
            return render(request, 'dice_game_app/index.html', {'message': f"Sorry, you lost with a score of {points}. Better luck next time, {player_name}!"})
    return render(request, 'dice_game_app/index.html')