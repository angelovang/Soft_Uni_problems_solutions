def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact


n1 = int(input())
n2 = int(input())
fac_1 = factorial(n1)
fac_2 = factorial(n2)
result = fac_1/fac_2
print(f'{result:.2f}')


