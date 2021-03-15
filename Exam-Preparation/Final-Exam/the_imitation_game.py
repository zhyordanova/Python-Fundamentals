def move(message, n):
    result = message[n:] + message[:n]
    return result


def insert(message, idx, val):
    result = message[:idx] + val + message[idx:]
    return result


def change(message, subs, repl):
    result = message.replace(subs, repl)
    return result


encrypted_message = input()

command_data = input()


while not command_data == "Decode":
    command_data = command_data.split("|")
    command = command_data[0]

    if command == "Move":
        number_letters = int(command_data[1])
        encrypted_message = move(encrypted_message, number_letters)
    elif command == "Insert":
        index = int(command_data[1])
        value = command_data[2]
        encrypted_message = insert(encrypted_message, index, value)
    elif command == "ChangeAll":
        substring = command_data[1]
        replacement = command_data[2]
        encrypted_message = change(encrypted_message, substring, replacement)

    command_data = input()

print(f"The decrypted message is: {encrypted_message}")