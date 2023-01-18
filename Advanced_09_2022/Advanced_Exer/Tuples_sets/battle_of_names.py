lines = int(input())
odd_set = set()
even_set = set()

for i in range(1,lines+1):
    name = input()
    sum = 0
    for ch in name:
        sum += ord(ch)
    res = sum // i
    if res % 2 == 0:
        even_set.add(res)
    else:
        odd_set.add(res)

odd_sum = 0
even_sum = 0
for a in odd_set :
    odd_sum += a
for b in even_set :
    even_sum += b

result = set()
if odd_sum == even_sum:
    result = odd_set.union(even_set)
elif odd_sum > even_sum:
    result = odd_set.difference(even_set)
elif odd_sum < even_sum:
    result = odd_set.symmetric_difference(even_set)

print(', '.join(map(str,result)))
