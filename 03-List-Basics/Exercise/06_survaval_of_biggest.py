numbers_str = input().split()

numbers = []

for num in numbers_str:
    numbers.append(int(num))

remover = int(input())

for i in range(remover):
    numbers.remove(min(numbers))

print(numbers)