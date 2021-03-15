task = {}

command = input()
while not command == "stop":
    value = int(input())
    if command not in task:
        task[command] = value
    else:
        task[command] += value

    # if command not in task:
    #     task[command] = 0
    #
    # task[command] += value

    command = input()

for resource, quantity in task.items():
    print(f'{resource} -> {quantity}')




