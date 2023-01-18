num_1 = int (input())
num_2 = int (input())
math_operator = input()

is_even = 'even'
result = 0

if math_operator == '+' or math_operator == '-' or math_operator == '*':
    if math_operator == '+' :
        result = num_1 + num_2
    elif math_operator == '-':
        result = num_1 - num_2
    elif math_operator == '*':
        result = num_1 * num_2

    if result % 2 == 1:
        is_even = 'odd'
    print(f'{num_1} {math_operator} {num_2} = {result} - {is_even}')
else:
    if num_2 == 0:
        print(f'Cannot divide {num_1} by zero')
    else:
        if math_operator == '/':
            result = num_1 / num_2
            print(f'{num_1} / {num_2} = {result:.2f}')
        elif math_operator == '%':
            result = num_1 % num_2
            print(f'{num_1} % {num_2} = {result}')






