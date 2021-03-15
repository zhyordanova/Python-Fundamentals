n = int(input())
word = input()
string = []
string_included = []

for i in range(n):
    current_string = input()
    string.append(current_string)
    if word in current_string:
        string_included.append(current_string)

print(string)
print(string_included)


# n = int(input())
# word = input()
#
# strings = []
# for i in range(n):
#     current_string = input()
#     strings.append(current_string)
# print(strings)
#
# for i in range(len(strings) - 1, -1, -1):
#     if word not in strings[i]:
#         strings.remove(strings[i])
# print(strings)
