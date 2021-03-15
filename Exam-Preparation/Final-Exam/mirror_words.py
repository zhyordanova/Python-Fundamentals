import re

string = input()
regex = r"(#|@)([a-zA-z]{3,})(\1{2})([a-zA-z]{3,})(\1)"
mirror_words = {}
final_list = []

words = re.findall(regex, string)

for word in words:
    if word[1][::-1] == word[3]:
        mirror_words[word[1]] = word[3]
        final_list.append(f"{word[1]} <=> {word[3]}")

if len(words) == 0:
    print(f"No word pairs found!")
else:
    print(f"{len(words)} word pairs found!")

if len(mirror_words) == 0:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")

print(", ".join(final_list))