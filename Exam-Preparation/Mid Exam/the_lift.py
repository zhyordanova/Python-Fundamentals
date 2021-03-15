n_people = int(input())
wagon = [int(el) for el in input().split()]

MAX_PEOPLE_PER_WAGON = 4


for index in range(len(wagon)):
    while not wagon[index] == MAX_PEOPLE_PER_WAGON:
        if n_people > 0:
            wagon[index] += 1
            n_people -= 1
        else:
            break

all_seats = len(wagon) * MAX_PEOPLE_PER_WAGON
taken_seats = sum(wagon)

if n_people == 0 and taken_seats < all_seats:
    print("The lift has empty spots!")
elif n_people > 0 and taken_seats == all_seats:
    print(f"There isn't enough space! {n_people} people in a queue!")
print(' '.join([str(el) for el in wagon]))
