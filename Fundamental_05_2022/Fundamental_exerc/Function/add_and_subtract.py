num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_numbers(a,b):
    return a+b


def subtract(s,c):
    return s-c


def add_and_subtract(a,b,c):
    return subtract(sum_numbers(a,b),c)

print(add_and_subtract(num_1,num_2,num_3))

