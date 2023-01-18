numbers_stack = []
lines = int(input())

for i in range(lines):
    command = input().split()
    cmd = command[0]

    if cmd == '1':
        numbers_stack.append(int(command[1]))

    if numbers_stack:
        if cmd == '2':
            numbers_stack.pop()
        elif cmd == '3':
            print(max(numbers_stack))
        elif cmd == '4':
            print(min(numbers_stack))

print(*numbers_stack[::-1],sep=', ')

'''
while numbers_stack:
    res = numbers_stack.pop()
    if numbers_stack:       #proverka za posleden red sled .pop()
        print(res,end=', ')
    else:
        print(res)
'''