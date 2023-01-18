expression = input()
stack_parent = []
for i in range(len(expression)):
    if expression[i] == '(':
        stack_parent.append(i)
    elif expression[i] == ')':
        start = stack_parent.pop()
        end = i+1
        print(expression[start:end])


