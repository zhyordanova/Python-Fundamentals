lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
counter_shield_brakes = 0

for game in range(1, lost_fights + 1):

    if game % 2 == 0:
        expenses += helmet_price

    if game % 3 == 0:
        expenses += sword_price

    if game % 2 == 0 and game % 3 == 0:
        expenses += shield_price
        counter_shield_brakes += 1

        if counter_shield_brakes % 2 == 0:
            expenses += armor_price


print(f'Gladiator expenses: {expenses:.2f} aureus')