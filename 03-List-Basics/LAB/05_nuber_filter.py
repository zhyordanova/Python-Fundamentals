n = int(input())
even_numbers = []
odd_numbers = []
negative_numbers = []
positive_numbers = []


for i in range(n):
    current_number = int(input())
    if current_number % 2 == 0:
        even_numbers.append(current_number)

    if not current_number % 2 == 0:
        odd_numbers.append(current_number)

    if current_number < 0:
        negative_numbers.append(current_number)

    if current_number >= 0:
        positive_numbers.append(current_number)

command = input()

if command == "even":
    print(even_numbers)
elif command == "odd":
    print(odd_numbers)
elif command == "negative":
    print(negative_numbers)
else:
    print(positive_numbers)


# n = int(input())
# numbers = []
# filtered = []
#
# for i in range(n):
#     current_number = int(input())
#     numbers.append(current_number)
#
# command = input()
#
# if command == "even":
#     for number in numbers:
#         if number % 2 == 0:
#             filtered.append(number)
# elif command == "odd":
#     for number in numbers:
#         if not number % 2 == 0:
#             filtered.append(number)
# elif command == "negative":
#     for number in numbers:
#         if number < 0:
#             filtered.append(number)
# if command == "positive":
#     for number in numbers:
#         if number >= 0:
#             filtered.append(number)
#
# print(filtered)