def characters_in_range(start, end):
    result = ''
    for i in range(ord(start) + 1, ord(end)):
        result += chr(i) + ' '
    return result


start_step = input()
end_step = input()
print(characters_in_range(start_step, end_step))
