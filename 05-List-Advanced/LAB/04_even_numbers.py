nums = list(map(int, input().split(', ')))
even_nums = list(filter(lambda index: nums[index] % 2 == 0, range(len(nums))))

print(even_nums)