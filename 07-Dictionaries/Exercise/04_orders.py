# # data = input()
# #
# # quantities_dict = {}
# # prices_dict = {}
# #
# # while not data == "buy":
# #     product, price, quantity = data.split()
# #     price = float(price)
# #     quantity = int(quantity)
# #
# #     prices_dict[product] = price
# #
# #     if product not in quantities_dict:
# #         quantities_dict[product] = 0
# #
# #     quantities_dict[product] += quantity
# #
# #     data = input()
# #
# #
# # for product_name, product_price in prices_dict.items():
# #     total_price = product_price * quantities_dict[product_name]
# #     print(f"{product_name} -> {total_price:.2f}")
#
#
# products = {}
#
# data = input()
#
# while not data == "buy":
#     product, price, quantity = data.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if product not in products:
#         products[product] = {'price': price, 'quantity': quantity}
#
#     else:
#         products[product]['price'] = price
#         products[product]['quantity'] += quantity
#
#
#     data = input()
#
# for product_name, price_quantity_data in products.items():
#     total_price = price_quantity_data['price'] * price_quantity_data['quantity']
#     print(f"{product_name} -> {total_price:.2f}")


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


data = input()
products = []

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    if name in map(lambda x: x.name, products):
        product = list(filter(lambda x: x.name == name, products))[0]
        product.price = price
        product.quantity += quantity
    else:
        product = Product(name, price, quantity)
        products.append(product)

    data = input()

for product in products:
    print(f"{product.name} -> {product.price * product.quantity:.2f}")