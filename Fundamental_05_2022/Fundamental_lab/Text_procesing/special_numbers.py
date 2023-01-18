num = int(input())
num_str = str(num)


for i in range(1,num+1):
    num_str = str(i)
    sum = 0
    special_number = False
    for dig in num_str :
        sum += int(dig)
    if sum == 5 or sum == 7 or sum == 11:
        special_number = True
    print(f'{i} -> {special_number}')

