line = input().upper()
unique_symbol = set()
return_string = ''
text = ''

for i in range(len(line)):
    if not line[i].isdigit():
        text += line[i]
    else:
        digit = ''
        while i < len(line) and line[i].isdigit():
            digit += line[i]
            i += 1
        return_string += text * int(digit)
        text = ''

print(f"Unique symbols used: {len(set(return_string))}")
print(return_string)
