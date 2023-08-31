import csv

player_scores = {}
with open("game_scores.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        nameP, score = row
        score = int(score)
        if nameP not in player_scores or score > player_scores[nameP]:
            player_scores[nameP] = score
sorted_scores = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)
with open("high_scores.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Player name", "Highest score"])
    writer.writerows(sorted_scores)
