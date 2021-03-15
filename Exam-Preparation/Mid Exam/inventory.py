def collect(journal_list, add_item):
    if add_item not in journal_list:
        journal_list.append(add_item)
    return journal_list


def drop(journal_list, remove_item):
    if remove_item in journal_list:
        journal_list.remove(remove_item)
    return journal_list


def combine(journal_list, old, new):
    if old in journal_list:
        old_idx = journal_list.index(old)
        journal_list.insert(old_idx + 1, new)
    return journal_list


def renew(journal_list, renew_item):
    if renew_item in journal_list:
        journal_list.remove(renew_item)
        journal_list.append(renew_item)
    return journal_list


journal = input().split(", ")

command_data = input()

while not command_data == "Craft!":
    command, item = command_data.split(" - ")

    if command == "Collect":
        journal = collect(journal, item)
    elif command == "Drop":
        journal = drop(journal, item)
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        journal = combine(journal, old_item, new_item)
    elif command == "Renew":
        journal = renew(journal, item)

    command_data = input()

print(", ".join(journal))