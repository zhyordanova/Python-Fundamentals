import re

pattern = r"(:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})\1"

text = input()

cool_threshold = 1
digits = re.findall(r"\d", text)

for digit in digits:
    cool_threshold *= int(digit)
print(f"Cool threshold: {cool_threshold}")

emojis = re.finditer(pattern, text)
match_emoji = [e.group() for e in emojis]
print(f"{len(match_emoji)} emojis found in the text. The cool ones are:")

cool_emoji = []
for emoji in match_emoji:
    emoji_coolness = 0
    for char in emoji:
        if char.isalpha():
            emoji_coolness += ord(char)
    if emoji_coolness > cool_threshold:
        cool_emoji.append(emoji)

for emoji in cool_emoji:
    print(emoji)





