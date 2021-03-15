def calc_factorial(n):
    result = 1
    for num in range(2, n + 1):
        result *= num

    return result


number_1 = int(input())
number_2 = int(input())

factorial_1 = calc_factorial(number_1)
factorial_2 = calc_factorial(number_2)

res = factorial_1 / factorial_2

print(f"{res:.2f}")
