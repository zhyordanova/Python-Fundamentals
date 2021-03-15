number = int(input())

result = 0

for i in range(number):
    character = input()
    result += ord(character)

print(f'The sum equals: {result}')


