def calc_factorial(n):
    res = 1
    for num in range(2, n + 1):
        res *= num

    return res


number_1 = int(input())
number_2 = int(input())

factorial_1 = calc_factorial(number_1)
factorial_2 = calc_factorial(number_2)

result = factorial_1 / factorial_2
print(f"{result:.2f}")
