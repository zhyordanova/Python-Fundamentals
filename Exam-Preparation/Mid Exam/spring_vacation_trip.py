days = int(input())
budget = float(input())
group_people = int(input())
price_fuel_per_km = float(input())
food_person_day = float(input())
room_person_night = float(input())

food_expenses = food_person_day * group_people * days
hotel_expenses = room_person_night * group_people * days

is_travelled = True
if group_people <= 10:
    expenses = food_expenses + hotel_expenses
else:
    expenses = food_expenses + (hotel_expenses * 0.75)

for day in range(1, days + 1):
    travel_distance = float(input())
    consume_fuel = travel_distance * price_fuel_per_km
    expenses += consume_fuel
    if budget >= expenses:
        if day % 3 == 0 or day % 5 == 0:
            expenses += expenses * 0.4

        if day % 7 == 0:
            expenses -= expenses / group_people

    if budget < expenses:
        is_travelled = False
        print(f"Not enough money to continue the trip. You need {expenses - budget:.2f}$ more.")
        break

if is_travelled:
    print(f"You have reached the destination. You have {budget - expenses:.2f}$ budget left.")
