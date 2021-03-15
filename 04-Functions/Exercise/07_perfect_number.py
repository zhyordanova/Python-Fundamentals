def is_perfect(n):
    divisors = []
    for num in range(1, n // 2 + 1):
        if n % num == 0:
            divisors.append(num)
    if sum(divisors) == n:
        return True
    return False


number = int(input())

if is_perfect(number):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')
