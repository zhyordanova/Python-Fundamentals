import math
biscuits_per_worker = int(input())
workers = int(input())
competing_factory = int(input())

production_per_month = 0

for day in range(1, 31):
    daily_product = biscuits_per_worker * workers

    if day % 3 == 0:
        daily_product *= 0.75

    production_per_month += math.floor(daily_product)

print(f'You have produced {int(production_per_month)} biscuits for the past month.')

difference = abs(production_per_month - competing_factory)
percentage = difference / competing_factory * 100

if production_per_month >= competing_factory:
    print(f'You produce {percentage:.2f} percent more biscuits.')
else:
    print(f'You produce {percentage:.2f} percent less biscuits.')




