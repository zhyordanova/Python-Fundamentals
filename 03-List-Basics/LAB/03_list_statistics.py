n = int(input())
positive_num = []
negative_num = []

for i in range(n):

    current_number = int(input())
    if current_number > 0:
        positive_num.append(current_number)
    else:
        negative_num.append(current_number)

print(positive_num)
print(negative_num)
print(f'Count of positives: {len(positive_num)}. Sum of negatives: {sum(negative_num)}')