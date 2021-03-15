def insert(raw_message, idx):
    result = raw_message[:idx] + " " + raw_message[index:]
    print(result)
    return result


def reverse(raw_message, subs):
    if subs not in raw_message:
        print("error")
    else:
        raw_message = raw_message.replace(subs, "", 1)
        raw_message += subs[::-1]
        print(raw_message)
    return raw_message


def change(raw_message, subs, repl):
    result = raw_message.replace(subs, repl)
    print(result)
    return result


concealed_message = input()

command_data = input()

while not command_data == "Reveal":
    data = command_data.split(":|:")
    command = data[0]

    if command == "InsertSpace":
        index = int(data[1])
        concealed_message = insert(concealed_message, index)
    elif command == "Reverse":
        substring = data[1]
        concealed_message = reverse(concealed_message, substring)
    elif command == "ChangeAll":
        substring, replacement = data[1:]
        concealed_message = change(concealed_message, substring, replacement)

    command_data = input()

print(f"You have a new text message: {concealed_message}")
