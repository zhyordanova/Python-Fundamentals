text = input()

result = [chr(ord(x) + 3) for x in text]

print(''.join(result))