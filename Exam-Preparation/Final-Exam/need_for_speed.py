def drive(cars_dict, car_name, drive_distance, needed_fuel):
    current_fuel = cars_dict[car_name]['fuel']
    if current_fuel < needed_fuel:
        print("Not enough fuel to make that ride")
    else:
        cars_dict[car_name]['mileage'] += drive_distance
        cars_dict[car_name]['fuel'] -= needed_fuel
        print(f"{car_name} driven for {drive_distance} kilometers. {needed_fuel} liters of fuel consumed.")
    if cars_dict[car_name]['mileage'] >= 100000:
        del cars_dict[car_name]
        print(f"Time to sell the {car_name}!")
    return cars_dict


def refuel(cars_dict, car_name, refill_fuel):
    current_fuel = cars_dict[car_name]['fuel']
    if current_fuel + refill_fuel > 75:
        cars_dict[car_name]['fuel'] = 75
        print(f"{car_name} refueled with {75 - current_fuel} liters")
    else:
        cars_dict[car_name]['fuel'] += refill_fuel
        print(f"{car_name} refueled with {refill_fuel} liters")
    return cars_dict


def revert(cars_dict, car_name, given_kilometers):
    if cars_dict[car_name]['mileage'] - given_kilometers < 10000:
        cars_dict[car_name]['mileage'] = 10000
    else:
        cars_dict[car_name]['mileage'] -= given_kilometers
        print(f"{car_name} mileage decreased by {given_kilometers} kilometers")
    return cars_dict


n = int(input())
cars = {}

for _ in range(n):
    car_inf = input().split('|')
    cars[car_inf[0]] = {'mileage': int(car_inf[1]), 'fuel': int(car_inf[2])}


data = input()

while not data == "Stop":
    splitted_data = data.split(" : ")
    command = splitted_data[0]

    if command == "Drive":
        car = splitted_data[1]
        distance = int(splitted_data[2])
        fuel_need = int(splitted_data[3])
        cars = drive(cars, car, distance, fuel_need)
    elif command == "Refuel":
        car = splitted_data[1]
        fuel_refill = int(splitted_data[2])
        cars = refuel(cars, car, fuel_refill)
    elif command == "Revert":
        car = splitted_data[1]
        kilometers = int(splitted_data[2])
        cars = revert(cars, car, kilometers)

    data = input()

sorted_cars = sorted(cars.items(), key=lambda x: (- x[1]['mileage'], x[0]))

for car, value in sorted_cars:
    print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")




