parent = input()
stack = []

for ch in parent:
    if not stack:
        stack.append(ch)
    else:
        if (ord(ch) == ord(stack[-1]) +1) or  (ord(ch) == ord(stack[-1]) +2) :
            stack.pop()
        else:
            stack.append(ch)
if stack:
    print('NO')
else:
    print('YES')




