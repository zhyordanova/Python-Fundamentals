data = input().split()

products = {}

for index in range(0, len(data), 2):
    product_name = data[index]
    product_quantity = int(data[index + 1])
    products[product_name] = product_quantity

products_to_search = input().split()

for product in products_to_search:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
