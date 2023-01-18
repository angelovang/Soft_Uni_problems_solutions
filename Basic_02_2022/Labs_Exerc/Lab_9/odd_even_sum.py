n = int(input())

even_sum = 0
odd_sum = 0

for i in range (n):
    num = int(input())
    if i % 2 == 0 :
        even_sum += num
    else:
        odd_sum += num



diff = even_sum - odd_sum

if diff == 0:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    print(f'No')
    print (f'Diff = {abs(diff)}')


