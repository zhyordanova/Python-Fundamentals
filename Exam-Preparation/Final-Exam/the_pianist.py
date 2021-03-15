def add(pieces_dict, p_add, c_add, k_add):
    if p_add in pieces_dict:
        print(f"{p_add} is already in the collection!")
    else:
        pieces_dict[p_add] = {'composer': c_add, 'key': k_add}
        print(f"{p_add} by {c_add} in {k_add} added to the collection!")
    return pieces_dict


def remove(pieces_dict, p_remove):
    if p_remove not in pieces_dict:
        print(f"Invalid operation! {p_remove} does not exist in the collection.")
    else:
        del pieces_dict[p_remove]
        print(f"Successfully removed {p_remove}!")
    return pieces_dict


def change(pieces_dict, p_change, new_k):
    if p_change not in pieces_dict:
        print(f"Invalid operation! {p_change} does not exist in the collection.")
    else:
        pieces_dict[p_change]['key'] = new_k
        print(f"Changed the key of {p_change} to {new_k}!")
    return pieces_dict


n = int(input())
pieces = {}

for _ in range(n):
    data = input().split("|")
    pieces[data[0]] = {'composer': data[1], 'key': data[2]}

command_data = input()


while not command_data == "Stop":
    command_data = command_data.split("|")
    command = command_data[0]

    if command == "Add":
        piece_add, composer_add, key_add = command_data[1:]
        pieces = add(pieces, piece_add, composer_add, key_add)
    elif command == "Remove":
        piece_remove = command_data[1]
        pieces = remove(pieces, piece_remove)
    elif command == "ChangeKey":
        piece_change, new_key = command_data[1:]
        pieces = change(pieces, piece_change, new_key)

    command_data = input()

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1]['composer']))

for piece, value in sorted_pieces:
    print(f"{piece} -> Composer: {value['composer']}, Key: {value['key']}")
