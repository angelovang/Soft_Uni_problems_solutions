def sum(number):
    number = str(number)
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for ch in number:
        if int(ch) % 2 == 0:
            sum_of_even_digits += int(ch)
        else:
            sum_of_odd_digits += int(ch)
    return sum_of_odd_digits,sum_of_even_digits
number = int(input())

a,b = sum(number)
print(f'Odd sum = {a}, Even sum = {b}')
