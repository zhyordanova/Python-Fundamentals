first = int(input())
second = int(input())
third = int(input())
students = int(input())

students_per_hour = first + second + third
hour = 0

while students > 0:
    students -= students_per_hour
    hour += 1

    if hour % 4 == 0:
        hour += 1

print(f"Time needed: {hour}h.")
