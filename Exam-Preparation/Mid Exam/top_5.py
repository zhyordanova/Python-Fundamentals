numbers = list(map(int, input().split()))
new_num = []

avg = sum(numbers) // len(numbers)

for i in range(len(numbers)):
    if numbers[i] > avg:
        new_num.append(numbers[i])
        new_num.sort(reverse=True)

if len(new_num) == 0:
    print("No")
else:
    print(*new_num[:5])