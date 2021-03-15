import re

line = input()

pattern = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"

names = re.findall(pattern, line)

print(*names)