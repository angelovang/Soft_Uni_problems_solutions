def get_primes(numbers: list):
    for number in numbers:
        if number <= 1:
            continue

        for x in range(2, number):
            if number % x == 0:
                break

        else:
            yield number

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))

