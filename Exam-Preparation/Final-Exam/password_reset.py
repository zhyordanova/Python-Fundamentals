def take_odd(raw_pass):
    result = ""
    for i in range(1, len(raw_pass), 2):
        result += raw_pass[i]
    print(result)
    return result


def cut(raw_pass, i, l):
    result = raw_pass[:i] + raw_pass[i+l:]
    print(result)
    return result


def substitute(raw_pass, s_str, repl):
    result = raw_pass.replace(s_str, repl)
    if result == raw_pass:
        print("Nothing to replace!")
    else:
        print(result)
    return result


password = input()

line = input()

while not line == "Done":
    data = line.split()
    command = data[0]

    if command == "TakeOdd":
        password = take_odd(password)
    elif command == "Cut":
        index, length = [int(el) for el in data[1:]]
        password = cut(password, index, length)
    elif command == "Substitute":
        sub_string, replacement = data[1:]
        password = substitute(password, sub_string, replacement)

    line = input()

print(f"Your password is: {password}")
