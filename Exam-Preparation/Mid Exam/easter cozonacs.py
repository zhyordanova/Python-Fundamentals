budget = float(input())
price_floor = float(input())

price_egg = price_floor * 0.75
price_milk = (price_floor * 1.25) / 4

price_cozonac = price_floor + price_egg + price_milk

cozonacs_count = 0
colored_eggs_count = 0


while budget >= price_cozonac:
    cozonacs_count += 1
    colored_eggs_count += 3


    if cozonacs_count % 3 == 0:
        colored_eggs_count -= cozonacs_count - 2

    budget -= price_cozonac

print(f'You made {cozonacs_count} cozonacs! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.')
