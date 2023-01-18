n = int(input())

left_sum = 0
right_sum = 0

for i in range (n):
    left_sum += int(input())

for i in range(n):
    right_sum += int(input())

diff = left_sum - right_sum

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(diff)}')

