number_1 = int(input())
number_2 = int(input())

number_3 = 0
print('Before:')
print(f'a = {number_1}')
print(f'b = {number_2}')

number_3 = number_1
number_1 = number_2
number_2 = number_3
print('After:')
print(f'a = {number_1}')
print(f'b = {number_2}')
