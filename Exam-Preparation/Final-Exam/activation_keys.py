def contains(raw_pass, substring):
    if substring not in raw_pass:
        print("Substring not found!")
    else:
        print(f"{raw_pass} contains {substring}")
    return raw_pass


def flip(raw_pass, case, start, end):
    result = ''
    if case == "Upper":
        result = raw_pass[:start] + raw_pass[start:end].upper() + raw_pass[end:]
        print(result)
    elif case == "Lower":
        result = raw_pass[:start] + raw_pass[start:end].lower() + raw_pass[end:]
        print(result)
    return result


def slice(raw_pass, start, end):
    result = ''
    result = raw_pass[:start] + raw_pass[end:]
    print(result)
    return result


activation_key = input()

line = input()

while not line == "Generate":
    data = line.split(">>>")
    command = data[0]

    if command == "Contains":
        substring = data[1]
        activation_key = contains(activation_key, substring)
    elif command == "Flip":
        case_sensitive = data[1]
        start = int(data[2])
        end = int(data[3])
        activation_key = flip(activation_key, case_sensitive, start, end)
    elif command == "Slice":
        start_index = int(data[1])
        end_index = int(data[2])
        activation_key = slice(activation_key, start_index, end_index)

    line = input()

print(f"Your activation key is: {activation_key}")