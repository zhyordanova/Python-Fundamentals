text = input()
result = ''
force = 0
i = 0

while i < len(text):
    if text[i] != ">":
        result += text[i]
        i += 1
    else:
        result += ">"
        i += 1
        force += int(text[i])

        while force > 0 and text[i] != ">":
            i += 1
            force -= 1
            if i >= len(text):
                break

print(result)

