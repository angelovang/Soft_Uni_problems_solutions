def fibonacci():
    num_1 = 0
    num_2 = 1

    while True:
        yield num_1

        num_1 , num_2 = num_2 , num_1 + num_2

generator = fibonacci()
for i in range(5):
    print(next(generator))

print('*'*10)

generator = fibonacci()
for i in range(1):
    print(next(generator))