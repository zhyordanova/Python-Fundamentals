lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet_counter = 0
broken_sword_counter = 0
broken_shield_counter = 0
broken_armor_counter = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        broken_helmet_counter += 1

    if i % 3 == 0:
        broken_sword_counter += 1

    if i % 6 == 0:
        broken_shield_counter += 1

    if i % 12 == 0:
        broken_armor_counter += 1

total_expenses = broken_helmet_counter * helmet_price \
                 + broken_sword_counter * sword_price \
                 + broken_shield_counter * shield_price \
                 + broken_armor_counter * armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
