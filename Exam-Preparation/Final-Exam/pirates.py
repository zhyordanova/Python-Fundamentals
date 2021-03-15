def plunder(cities_dict, town_name, people_count, gold_amount):
    current_population = cities_dict[town_name]["population"]
    current_gold = cities_dict[town_name]["gold"]
    cities_dict[town_name]["population"] -= people_count
    cities_dict[town_name]["gold"] -= gold_amount
    print(f"{town_name} plundered! {gold_amount} gold stolen, {people_count} citizens killed.")
    if cities_dict[town_name]["population"] <= 0 or cities_dict[town_name]["gold"] <= 0:
        del cities_dict[town_name]
        print(f"{town_name} has been wiped off the map!")
    return cities_dict


def prosper(cities_dict, city, gold_add):
    if gold_add < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities_dict[city]["gold"] += gold_add
        print(f"{gold_add} gold added to the city treasury. {city} now has {cities_dict[city]['gold']} gold.")
    return cities_dict


command_data = input()

cities = {}

while not command_data == "Sail":
    name, population, gold = command_data.split("||")
    population = int(population)
    gold = int(gold)
    if name not in cities:
        cities[name] = {"population": population, "gold": gold}
    else:
        cities[name]["population"] += population
        cities[name]["gold"] += gold

    command_data = input()

events_data = input()

while not events_data == "End":
    events = events_data.split("=>")
    event = events[0]
    town = events[1]

    if event == "Plunder":
        people = int(events[2])
        gold_stolen = int(events[3])
        cities = plunder(cities, town, people, gold_stolen)
    elif event == "Prosper":
        gold_add = int(events[2])
        cities = prosper(cities, town, gold_add)
    events_data = input()


sorted_cities = sorted(cities.items(), key=lambda x: (- x[1]["gold"], x[0]))

if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, value in sorted_cities:
        print(f"{city} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")

