number = int(input())

def is_perfect_number(n):
    sum_of_divisors = 0
    current_n = n
    while current_n > 1:
        current_n -= 1
        if n % current_n == 0:
            sum_of_divisors += current_n
    if sum_of_divisors == n:
        return 'We have a perfect number!'
    return 'It\'s not so perfect.'

print(is_perfect_number(number))


