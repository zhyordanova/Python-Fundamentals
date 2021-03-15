words = input().split()


def delete_word(index):
    if index + 1 in range(len(words)):
        words.remove(words[index + 1])
    return words


def swap_word(word_1, word_2):
    if word_1 in words and word_2 in words:
        index1 = words.index(word_1)
        index2 = words.index(word_2)
        words[index1], words[index2] = words[index2], words[index1]
    return words


def put_word(word, index):
    if 0 <= index - 1 <= len(words):
        words.insert(index - 1, word)
    return words


def sort_word():
    return words.sort(reverse=True)


def replace_word(word1, word2):
    if word2 in words:
        i = words.index(word2)
        words[i] = word1
    return words


command = input()

while not command == "Stop":
    action = command.split()[0]


    if action == "Delete":
        index = int(command.split()[1])
        delete_word(int(index))

    elif action == "Swap":
        word_1 = command.split()[1]
        word_2 = command.split()[2]
        swap_word(word_1, word_2)

    elif action == "Put":
        word_1 = command.split()[1]
        index = int(command.split()[2])
        put_word(word_1, int(index))

    elif action == "Sort":
        sort_word()

    elif action == "Replace":
        word_1 = command.split()[1]
        word_2 = command.split()[2]
        replace_word(word_1, word_2)

    command = input()

print(' '.join(words))
