def simple_calculations(oper, num_1, num_2):
    result = 0
    if oper == 'multiply':
        result = num_1 * num_2
    elif oper == 'divide':
        result = num_1 // num_2
    elif oper == 'add':
        result = num_1 + num_2
    elif oper == 'subtract':
        result = num_1 - num_2
    return result


operator = input()
number_1 = int(input())
number_2 = int(input())
print(simple_calculations(operator, number_1, number_2))
