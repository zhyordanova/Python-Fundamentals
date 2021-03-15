string = input()
practice_sessions = {}

while not string == "END":
    item = string.split('->')
    command, road = item[0], item[1]
    if command == "Add":
        racer = item[2]
        if road not in practice_sessions:
            practice_sessions[road] = []
        practice_sessions[road]. append(racer)

    elif command == "Move":
        racer, next_road = item[2], item[3]
        if racer in practice_sessions[road]:
            practice_sessions[road].remove(racer)
            practice_sessions[next_road].append(racer)

    elif command == "Close":
        if road in practice_sessions:
            del practice_sessions[road]

    string = input()

print("Practice sessions:")

sort_practice_session = dict(sorted(sorted(practice_sessions.items()), key=lambda x: len(x[1]), reverse=True))

for racer, roads in sort_practice_session.items():
    print(racer)
    for road in roads:
        print(f'++{road}')