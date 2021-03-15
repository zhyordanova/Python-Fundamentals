def calculate_orders(item, quantity):
    price = 0
    if item == 'coffee':
        price = quantity * 1.50
    elif item == 'water':
        price = quantity * 1.00
    elif item == 'coke':
        price = quantity * 1.40
    elif item == 'snacks':
        price = quantity * 2.00
    return price


product = input()
product_quantity = int(input())
print(f'{calculate_orders(product, product_quantity):.2f}')
