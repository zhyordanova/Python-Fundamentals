paintings = list(map(int, input().split()))
command = input()

while not command == "END":
    command = command.split()

    if command[0] == "Change":
        change_painting_number = int(command[1])
        change_changed_number = int(command[2])
        if change_painting_number in paintings:
            index1 = paintings.index(change_painting_number)
            paintings[index1] = change_changed_number

    elif command[0] == "Hide":
        hide_painting_number = int(command[1])
        if hide_painting_number in paintings:
            paintings.remove(hide_painting_number)

    elif command[0] == "Switch":
        switch_painting_number = int(command[1])
        switch_painting_number_2 = int(command[2])
        if switch_painting_number in paintings and switch_painting_number_2 in paintings:
            index_switch_painting_number = paintings.index(switch_painting_number)
            index_switch_painting_number_2 = paintings.index(switch_painting_number_2)
            paintings[index_switch_painting_number], paintings[index_switch_painting_number_2] = \
                paintings[index_switch_painting_number_2], paintings[index_switch_painting_number]

    elif command[0] == "Insert":
        insert_index = int(command[1])
        insert_painting_number = int(command[2])
        if insert_index in range(len(paintings)):
            paintings.insert(insert_index + 1, insert_painting_number)

    elif command[0] == "Reverse":
        paintings = paintings[::-1]

    command = input()

print(' '.join(list(map(str, paintings))))


