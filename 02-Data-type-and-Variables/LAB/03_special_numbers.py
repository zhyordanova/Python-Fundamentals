number = int(input())

for num in range(1, number + 1):
    digit_sum = 0
    for digit in str(num):
        digit_sum += int(digit)
    is_spacial = digit_sum in [5, 7, 11]
    print(f'{num} -> {is_spacial}')



