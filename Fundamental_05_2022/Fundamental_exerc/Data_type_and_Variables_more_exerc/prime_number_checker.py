from math import sqrt
number = int(input())
square_number = int (sqrt(number))

if number < 2 :
    print('False')
else:
    for i in range(2,square_number+1):
        if number % i == 0:
            print('False')
            break
    else:
        print('True')

