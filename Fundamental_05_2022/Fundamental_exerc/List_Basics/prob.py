def type_of_grade(num):
    if num == 2.00 or num <= 2.99:
        print("Fail")
    elif num == 3.00 or num <= 3.49:
        print("Poor")
    elif num == 3.50 or num <= 4.49:
        print("Good")
    elif num == 4.50 or num <= 5.49:
        print("Very Good")
    else:
        print("Excellent")


number = float(input())
print(type_of_grade(number))


# primer za kalkulator :
def calculator(num1, num2, operator):
    calc_dict = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y
    }

    return calc_dict[operator](num1, num2)


a = int(input())
b = int(input())
operator_input = input()

print(calculator(a, b, operator_input))
