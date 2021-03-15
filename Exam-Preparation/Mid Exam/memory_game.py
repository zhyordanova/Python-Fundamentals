def play_round(cards, el_1, el_2, g):
    if el_1 == el_2 or el_1 not in range(len(cards)) or el_2 not in range(len(cards)):
        print("Invalid input! Adding additional elements to the board")
        card = f"-{g}a"
        middle = len(cards) // 2
        cards.insert(middle, card)
        cards.insert(middle + 1, card)
    else:
        if cards[el_1] == cards[el_2]:
            element = cards[el_1]
            cards.remove(element)
            cards.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")
    return cards


memory_card = input().split()
line = input()
game = 0

while not line == "end":
    element_1, element_2 = [int(el) for el in line.split()]
    game += 1
    memory_card = play_round(memory_card, element_1, element_2, game)
    if len(memory_card) == 0:
        print(f"You have won in {game} turns!")
        exit(0)

    line = input()

print("Sorry you lose :(")
print(' '.join(memory_card))