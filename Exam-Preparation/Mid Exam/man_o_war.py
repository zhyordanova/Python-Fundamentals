pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())

lost = False

command = input()

while not command == "Retire":
    tokens = command.split()

    if tokens[0] == "Fire":
        index = int(tokens[1])
        damage = int(tokens[2])
        if 0 <= index <= len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                lost = True
                break

    elif tokens[0] == "Defend":
        start = int(tokens[1])
        end = int(tokens[2])
        damage = int(tokens[3])
        if 0 <= start < len(pirate_ship) and 0 <= end < len(pirate_ship):
            for index in range(start, end + 1):
                pirate_ship[index] -= damage
                if pirate_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    lost = True
                    break
            if lost:
                break

    elif tokens[0] == "Repair":
        index= int(tokens[1])
        health= int(tokens[2])
        if 0 <= index < len(pirate_ship):
            # if pirate_ship[index] + health > max_health:
            #     health = max_health - pirate_ship[index]
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health
                
    elif tokens[0] == "Status":
        minimum = max_health * 0.2
        count = len([x for x in pirate_ship if x < minimum])
        print(f"{count} sections need repair.")

    command = input()

if not lost:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
