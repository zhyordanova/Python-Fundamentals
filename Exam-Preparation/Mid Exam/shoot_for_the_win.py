targets = list(map(int, input().split('!')))

command = input()
count = 0

while not command == "End":
    index = int(command)

    if index in range(len(targets)):
        current_index = targets[index]
        for i in range(len(targets)):
            if not targets[i] == -1:
                if targets[i] > current_index:
                    targets[i] -= current_index
                else:
                    targets[i] += current_index
            targets[index] = -1
        count += 1

    command = input()

print(f"Shot targets: {count} -> {' '.join(map(str, targets))}")
