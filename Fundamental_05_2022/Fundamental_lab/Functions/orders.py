product = input()
quantity = int(input())


def calculator(a, b):
    result = None
    if a == "coffee":
        result = b * 1.50
    elif a == "water":
        result = b * 1.00
    elif a == "coke":
        result = b * 1.40
    elif a == "snacks":
        result = b * 2.0
    return result

print(f'{calculator(product,quantity):.2f}')
