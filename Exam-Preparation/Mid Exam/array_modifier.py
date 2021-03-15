array = list(map(int, input().split()))

line = input()

while not line == "end":
    command = line.split()[0]

    if command == "swap":
        index_1 = int(line.split()[1])
        index_2 = int(line.split()[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]
    elif command == "multiply":
        idx_1 = int(line.split()[1])
        idx_2 = int(line.split()[2])
        array[idx_1] *= array[idx_2]
    elif command == "decrease":
        array = [x - 1 for x in array]

    line = input()

print(', '.join(map(str, array)))






















