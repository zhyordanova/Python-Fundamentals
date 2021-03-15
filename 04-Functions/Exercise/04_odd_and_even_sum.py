def odd_and_even_sum(text):
    odd_sum = 0
    even_sum = 0
    for ch in text:
        number = int(ch)
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


num_text = input()
print(odd_and_even_sum(num_text))
