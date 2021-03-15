shops = input().split()


def include_shop(shop):
    shops.append(shop)
    return shops


def visit_shop(position, number):
    if len(shops) >= number:
        if position == 'first':
            del shops[:number]
        else:
            del shops[-number:]
    return shops


def prefer_shop(shop1, shop2):
    if shop1 in range(len(shops)) and shop2 in range(len(shops)):
        shops[shop1], shops[shop2] = shops[shop2], shops[shop1]
    return shops


def place_shop(shop, index):
    if index in range(len(shops)):
        shops.insert(index + 1, shop)
    return shops


number_commands = int(input())

for i in range(1, number_commands + 1):
    command = input()

    if "Include" in command:
        action, shop = command.split()
    else:
        action, shop, index = command.split()

    if action == 'Include':
        include_shop(shop)
    elif action == 'Visit':
        visit_shop(shop, int(index))
    elif action == 'Prefer':
        prefer_shop(int(shop), int(index))
    else:
        place_shop(shop, int(index))


print(f"Shops left:\n{' '.join(shops)}")
