users = input().split(', ')

for user in users:
    if 3 <= len(user) <= 16 and (user.isalnum() or '_' in user or '-' in user):
        print(user)



