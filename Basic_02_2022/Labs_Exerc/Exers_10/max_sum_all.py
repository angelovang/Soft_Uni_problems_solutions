count = int (input())
sum_all = 0
max_num = ''
for i  in range (count):
    curent_num = int(input())
    if i == 0:
        max_num = curent_num
    sum_all += curent_num
    if curent_num > max_num:
        max_num = curent_num

diff = max_num - (sum_all - max_num)

if max_num == sum_all - max_num :
    print ('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs(diff)}')

