from sys import maxsize
num_str = input()
min_num = maxsize
while num_str != 'Stop':
    num_int = int(num_str)
    if num_int < min_num :
        min_num = num_int
    num_str = input()
print(min_num)


