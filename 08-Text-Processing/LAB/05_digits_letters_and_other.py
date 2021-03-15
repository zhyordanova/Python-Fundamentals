letters = []
digits = []
others = []

line = input()

for char in line:
    if char.isalpha():
        letters.append(char)
    elif char.isdigit():
        digits.append(char)
    else:
        others.append(char)

print(''.join(digits))
print(''.join(letters))
print(''.join(others))


# letters = ''
# digits = ''
# others = ''
#
# line = input()
#
# for char in line:
#     if char.isalpha():
#         letters += char
#     elif char.isdigit():
#         digits += char
#     else:
#         others += char
#
# print(digits)
# print(letters)
# print(others)