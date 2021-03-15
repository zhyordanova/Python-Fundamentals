friends = input().split(', ')

command = input().split()
# blacklisted_count = 0
# lost_count = 0

while not command[0] == "Report":
    if command[0] == "Blacklist":
        name = command[1]
        if name in friends:
            friends[friends.index(name)] = "Blacklisted"
            print(f"{name} was blacklisted.")
            # blacklisted_count += 1
        else:
            print(f"{name} was not found.")


    elif command[0] == 'Error':
        index = int(command[1])
        if index in range(len(friends)):
            current_name = friends[index]
            if current_name != "Blacklisted" and current_name != "Lost":
                friends[index] = "Lost"
                print(f"{current_name} was lost due to an error.")
                # lost_count += 1

    elif command[0] == 'Change':
        index = int(command[1])
        if index in range(0, len(friends)):
            new_name = command[2]
            current_name = friends[index]
            friends[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")

    command = input().split()

blacklisted_count = len([name for name in friends if name == "Blacklisted"])
lost_count = len([name for name in friends if name == "Lost"])

print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_count}")
print(" ".join(friends))
