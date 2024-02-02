import os
import json
import random

def roll_dice():
    return random.randint(1, 6)
os.system('cls' if os.name == 'nt' else 'clear')
def play_game(points_to_win):
    os.system('cls' if os.name == 'nt' else 'clear')
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
        os.system('cls' if os.name == 'nt' else 'clear')

def load_top_games(points_to_win):
    filename = f'top_games_{points_to_win}.json'
    try:
        with open(filename, 'r') as f:
            top_games = json.load(f)
    except FileNotFoundError:
        top_games = []
    return top_games

def save_top_games(top_games, points_to_win):
    filename = f'top_games_{points_to_win}.json'
    with open(filename, 'w') as f:
        json.dump(top_games, f)

def display_top_games(top_games):
    print("Top 5 Games:")
    print("-" * 21)
    print("Rank  | Player          | Points | Rolls")
    print("-" * 21)
    for i, game in enumerate(reversed(top_games), start=1):
        print(f"{i:3}  | {game['player']:12} | {game['points']:5} | {game['rolls']:5}")
    print("-" * 21)

def main():
    player_name = input("Enter your name: ")
    points_to_win = int(input("Enter the number of points you want to play: "))
    again = input(f"Do you want to play a game of rolling a dice to get {points_to_win} points or less, {player_name}? (y/n) ")
    top_games = load_top_games(points_to_win)
    while again.lower() == 'y':
        points, rolls = play_game(points_to_win)
        if points < points_to_win:
            print(f"Congratulations! You won with a score of {points} in {rolls} rolls!")
            top_games.append({'player': player_name, 'points': points, 'rolls': rolls})
            top_games = sorted(top_games, key=lambda x: x['points'])[:5]
            save_top_games(top_games, points_to_win)
        elif points > points_to_win:
            print(f"Sorry, you lost with a score of {points}. Better luck next time, {player_name}!")
        display_top_games(top_games)
        player_name = input("Enter your name: ")
        points_to_win = int(input("Enter the number of points you want to play: "))
        again = input(f"Do you want to play a game of rolling a dice to get {points_to_win} points or less, {player_name}? (y/n) ")
    print(f"Thanks for playing, {player_name}!")

if __name__ == "__main__":
    main()