prices = input()

total_price = 0

while not prices == "special" and not prices == "regular":
    prices = float(prices)

    if prices < 0:
        print("Invalid price!")
    else:
        total_price += prices

    prices = input()

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    taxes = total_price * 0.2
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if prices == "special":
        discount = (total_price + taxes) * 0.9
        print(f"Total price: {discount:.2f}$")
    else:
        print(f"Total price: {(total_price + taxes):.2f}$")























