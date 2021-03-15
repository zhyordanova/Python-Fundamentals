strings = input().split()

strings_1 = strings[0]
strings_2 = strings[1]

total_sum = 0

for i in range(max(len(strings_1), len(strings_2))):
    if i < len(strings_1) and i < len(strings_2):
        total_sum += ord(strings_1[i]) * ord(strings_2[i])
    else:
        if i < len(strings_1):
            total_sum += ord(strings_1[i])
        else:
            total_sum += ord(strings_2[i])

print(total_sum)
