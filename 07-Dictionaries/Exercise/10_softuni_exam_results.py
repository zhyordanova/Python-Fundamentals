data = input()

exam = {}

while not data == "exam finished":
    data_list = data.split("-")


    if len(data_list) == 3:
        user_name, language, points = data.split("-")
        points = int(points)
        if user_name not in exam:
            exam[user_name] = {'language': language, 'points': points}
            if language in exam[user_name]['language']:
                exam[user_name]['language'] = language
                if points > exam[user_name]['points']:
                    exam[user_name]['points'] = points
    else:
        user_name, command = data.split("-")
        if command == "banned":
            del(exam[user_name])

    data = input()

sorted_results = sorted(exam.items(), key=lambda x: (-x[1]['points'], x[0]))

print("Results:")
for user, points in sorted_results:
    print(f"{user} | {points['points']}")


print("Submissions:")
sorted_submissions = sorted(exam.items(), key=lambda x: (- len(x[1]['language']), x[0]))
for user_name, value in sorted_submissions:
    print(f"{value['language']} – {len(value['language'])}")

# command = input()
# languages = {}
# users_points = {}
#
# while command != 'exam finished':
#     command = command.split('-')
#     user = command[0]
#     if command[1] != 'banned':
#         language = command[1]
#         points = int(command[2])
#         if language not in languages:
#             languages[language] = 1
#         else:
#             languages[language] += 1
#         if user not in users_points:
#             users_points[user] = points
#         else:
#             if points > users_points[user]:
#                 users_points[user] = points
#     else:
#         language = command[1]
#         users_points.pop(user)
#
#     command = input()
#
# users_points = dict(sorted(users_points.items(), key=lambda s: (-s[1], s[0])))
# languages = dict(sorted(languages.items(), key=lambda s: (-s[1], s[0])))
#
# print('Results:')
# for user, points in users_points.items():
#     print(f'{user} | {points}')
#
# print('Submissions:')
# for language, submissions in languages.items():
#     print(f'{language} - {submissions}')