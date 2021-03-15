words = input()


occurrences = {}

# for char in words:
#     if char == " ":
#         continue
#
#     if char not in occurrences:
#         occurrences[char] = 0
#
#     occurrences[char] += 1



for char in words:
    keys = occurrences.keys()
    if char in keys:
        occurrences[char] += 1
    else:
        occurrences[char] = 1

for character, occurrence in occurrences.items():
    if not character == ' ':
        print(f"{character} -> {occurrence}")
