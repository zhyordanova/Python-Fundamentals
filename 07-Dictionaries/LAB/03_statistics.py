product_data = input()

products = {}

while not product_data == "statistics":
    product, quantity = product_data.split(": ")
    quantity = int(quantity)
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

    product_data = input()

print("Products in stock:")
for product_name, product_quantity in products.items():
    print(f"- {product_name}: {product_quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products)}")