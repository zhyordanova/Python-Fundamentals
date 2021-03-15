health = 100
bitcoins = 0
dungeons_rooms = input().split("|")

for i in range(len(dungeons_rooms)):
    room = dungeons_rooms[i]
    args = room.split()
    command = args[0]
    number = int(args[1])

    if command == "potion":
        current_health = health
        health += number
        healed = number

        if health > 100:
            health = 100
            healed = 100 - current_health

        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i + 1}")
            exit(0)

print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
