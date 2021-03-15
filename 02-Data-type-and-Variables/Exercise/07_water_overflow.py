n = int(input())

capacity = 255

for i in range(n):
    litters = int(input())

    if capacity - litters < 0:
        print('Insufficient capacity!')
    else:
        capacity -= litters

print(255 - capacity)
