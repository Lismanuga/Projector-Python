import csv
import random


players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
player_scores = []
for player in players:
    for _ in range(100):
        score = random.randint(0, 1000)
        player_scores.append([player, score])
with open("game_scores.csv", mode="w") as file:
    writer = csv.writer(file)
    writer.writerow(["Player name", "Score"])
    writer.writerows(player_scores)
