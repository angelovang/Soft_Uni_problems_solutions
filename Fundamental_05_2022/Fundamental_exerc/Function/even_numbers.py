#numbers = input().split()
dig_numbers = [int(n) for n in input().split()]


def even(n):
    if n % 2 == 0:
        return True


print(list(filter(even,dig_numbers)))
