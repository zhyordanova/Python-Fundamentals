data = input()
practice_sessions = {}

while not data == "END":
    splitted_data = data.split('->')
    command = splitted_data[0]
    road = splitted_data[1]

    if command == "Add":
        racer = splitted_data[2]
        if road not in practice_sessions:
            practice_sessions[road] = []
        practice_sessions[road].append(racer)

    elif command == "Move":
        racer, next_road = splitted_data[2:]
        if racer in practice_sessions[road]:
            practice_sessions[road].remove(racer)
            practice_sessions[next_road].append(racer)

    elif command == "Close":
        if road in practice_sessions:
            del practice_sessions[road]

    data = input()

sorted_practice_sessions = sorted(practice_sessions.items(), key=lambda x: (- len(x[1]), x[0]))

print("Practice sessions:")
for racer, roads in sorted_practice_sessions:
    print(racer)
    for road in roads:
        print(f"++{road}")