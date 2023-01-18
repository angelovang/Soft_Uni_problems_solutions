operator = input()
first_num = int(input())
second_num = int(input())

def calculator(oper , x , y):
    result = None
    if oper == 'multiply':
        result = x * y
    elif oper == 'divide':
        result = int(x/y)
    elif oper == 'add':
        result = x+y
    elif oper == 'subtract':
        result = x-y
    return result

print(calculator(operator,first_num,second_num))

