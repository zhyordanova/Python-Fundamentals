factor = int(input())
counter = int(input())

nums = []
for num in range(factor, factor * counter + 1, factor):
    nums.append(num)

print(nums)