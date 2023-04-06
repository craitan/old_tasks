command = input().split(' ')
team_a = 11
team_b = 11
condition = False
players_cards = []
for card in command:
    if card not in players_cards:
        players_cards.append(card)
        if 'A' in card:
            team_a -= 1
        else:
            team_b -= 1

        if team_a < 7 or team_b < 7:
            condition = True
            break

print(f"Team A - {team_a}; Team B - {team_b}")
if condition:
    print("Game was terminated")