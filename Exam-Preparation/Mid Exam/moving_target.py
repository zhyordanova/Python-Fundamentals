def is_target_exist(targets_list, idx):
    return True if idx in range(len(targets_list)) else False


def shoot(targets_list, idx, val):
    if is_target_exist(targets_list, idx):
        targets_list[idx] -= val
        if targets_list[idx] <= 0:
            targets_list.pop(idx)
    return targets_list


def add(targets_list, idx, val):
    if not is_target_exist(targets_list, idx):
        print("Invalid placement!")
    else:
        targets_list.insert(idx, val)
    return targets


def strike(targets_list, idx, val):
    left_side = idx - val
    right_side = idx + val
    if left_side >= 0 and right_side <= len(targets_list):
        targets_list = targets_list[:left_side] + targets_list[right_side + 1:]
    else:
        print("Strike missed!")
    return targets_list


targets = list(map(int, input().split()))

line = input()

while not line == "End":
    command = line.split()[0]
    index = int(line.split()[1])
    value = int(line.split()[2])

    if command == "Shoot":
        targets = shoot(targets, index, value)
    elif command == "Add":
        targets = add(targets, index, value)
    elif command == "Strike":
        targets = strike(targets, index, value)

    line = input()

print('|'.join(map(str, targets)))
