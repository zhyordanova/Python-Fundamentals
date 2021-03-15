text = input()

index = 0

while index < len(text) - 1:
    if text[index] == text[index + 1]:
        text = text.replace(f"{text[index]}{text[index +1]}", f"{text[index]}")
        index -= 1
    index += 1

print(text)


