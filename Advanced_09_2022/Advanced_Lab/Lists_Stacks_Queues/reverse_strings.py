stack = list(input())
result = []
for i in range (len(stack),0,-1):
    result.append(stack.pop())
print(''.join(result))
