import re

pattern = r"(\||\#)(?P<item>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9][0-9]{0,3}|10000)\1"

data = input()


matches = re.finditer(pattern, data)
foods = []
calories = 0

for match in matches:
    obj = match.groupdict()
    foods.append(obj)
    calories += int(obj['calories'])

days = calories // 2000
print(f"You have food to last you for: {days} days!")

for food in foods:
    print(f"Item: {food['item']}, Best before: {food['date']}, Nutrition: {food['calories']}")


