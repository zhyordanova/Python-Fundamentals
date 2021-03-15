def is_palindrome(element):
    reversed_element = element[::-1]
    if element == reversed_element:
        return True
    return False


def separate_elements(text, sep):
    number_as_string = text.split(sep)
    return number_as_string


data = input()
number_string = separate_elements(data, ", ")

for el in number_string:
    print(is_palindrome(el))
