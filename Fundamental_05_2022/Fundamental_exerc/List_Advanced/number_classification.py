numbers = input().split(', ')


def positive(num_list):
    return [num  for num  in num_list if int(num ) >= 0]


def negative(num_list):
    return [num for num in num_list if int(num) < 0]


def even(num_list):
    return [num for num in num_list if int(num) % 2 == 0]


def odd(num_list):
    return [num for num in num_list if int(num) % 2 != 0]


print(f"Positive: {', '.join(positive(numbers))}")
print(f"Negative: {', '.join(negative(numbers))}")
print(f"Even: {', '.join(even(numbers))}")
print(f"Odd: {', '.join(odd(numbers))}")


