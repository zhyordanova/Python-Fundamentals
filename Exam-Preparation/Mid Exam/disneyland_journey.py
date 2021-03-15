journey_cost = float(input())
number_of_months = int(input())

saving = 0
spend = 0

for mon in range(1, number_of_months + 1):

    if mon % 2 == 1 and not mon == 1:
        spend = saving * 0.16
        saving -= spend

    if mon % 4 == 0:
        saving = (saving * 0.25) + saving

    saving += 0.25 * journey_cost

if saving > journey_cost:
    souvenirs = saving - journey_cost
    print(f"Bravo! You can go to Disneyland and you will have {souvenirs:.2f}lv. for souvenirs.")
else:
    needed_money = journey_cost - saving
    print(f"Sorry. You need {needed_money:.2f}lv. more.")