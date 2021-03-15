numbers_as_string = input().split()
sorted_number = sorted(numbers_as_string, reverse=True)

print(''.join(sorted_number))