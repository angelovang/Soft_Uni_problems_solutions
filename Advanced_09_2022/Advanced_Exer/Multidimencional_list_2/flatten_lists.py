start_list = input().split('|')
result = []
for y in start_list[::-1]:
    result.extend(y.split())

print(*result)

