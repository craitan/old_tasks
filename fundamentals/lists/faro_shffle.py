cards = input().split(" ")
shuffles = int(input())

for x in range(shuffles):
    deck1 = cards[:len(cards) // 2]
    deck2 = cards[len(cards) // 2:]
    cards = [deck for deck in zip(deck1, deck2) for deck in deck]
print(cards)