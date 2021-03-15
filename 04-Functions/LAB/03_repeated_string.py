def repeated_string(string, rep):
    result = ''
    for i in range(0, rep):
        result += string
    return result


string_input = input()
repeat = int(input())
print(repeated_string(string_input, repeat))
