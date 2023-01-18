import sys
n = int(input())

num_max = - sys.maxsize
num_min = sys.maxsize

for i in range (n):
    num = int(input())
    if num > num_max:
        num_max = num
    if num < num_min:
        num_min = num

print(f'Max number: {num_max}')
print(f'Min number: {num_min}')


