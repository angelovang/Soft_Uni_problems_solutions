count_nums = int(input())
p1=0
p2=0
p3=0
p4=0
p5=0
for x in range (count_nums):
    curent_num = int(input())
    if curent_num < 200:
        p1 += 1
    elif 200 <= curent_num < 400:
        p2 += 1
    elif 400 <= curent_num < 600:
        p3 += 1
    elif 600 <= curent_num < 800:
        p4 += 1
    else:
        p5 += 1

print(f'{(p1/count_nums*100):.2f}%')
print(f'{p2/count_nums*100:.2f}%')
print(f'{p3/count_nums*100:.2f}%')
print(f'{p4/count_nums*100:.2f}%')
print(f'{p5/count_nums*100:.2f}%')

