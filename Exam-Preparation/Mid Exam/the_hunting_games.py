days = int(input())
players = int(input())
energy = float(input())
water_day_person = float(input())
food_day_person = float((input()))

water = days * players * water_day_person
food = days * players * food_day_person

for day in range(1, days + 1):
    loss_energy = float(input())
    energy -= loss_energy

    if energy <= 0:
        break

    if day % 2 == 0:
        energy *= 1.05
        water *= 0.7

    if day % 3 == 0:
        energy *= 1.1
        food -= food / players

if energy > 0:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")


