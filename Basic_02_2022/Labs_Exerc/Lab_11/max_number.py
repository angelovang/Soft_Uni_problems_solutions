from sys import maxsize
num_str = input()
max_num = - maxsize
while num_str != 'Stop':
    num_int = int(num_str)
    if num_int > max_num :
        max_num = num_int
    num_str = input()
print(max_num)


