from collections import deque
from math import floor
text_expr = deque(txt for txt in input().split())
temp_expr = deque()
operators = '*,+,-,/'
res = 0

while text_expr:
    tmp = text_expr.popleft()
    if tmp not in operators:
        temp_expr.append(int(tmp))
    else:
        if tmp == '+':
            res = temp_expr.popleft()
            while temp_expr:
                res += temp_expr.popleft()
            text_expr.appendleft(str(res))
        elif tmp == '-':
            res = temp_expr.popleft()
            while temp_expr:
                res -= temp_expr.popleft()
            text_expr.appendleft(str(res))
        elif tmp == '*':
            res = temp_expr.popleft()
            while temp_expr:
                res *= temp_expr.popleft()
            text_expr.appendleft(str(res))
        elif tmp == '/':
            res = temp_expr.popleft()
            while temp_expr:
                d = temp_expr.popleft()
                res = floor(res / d)
            text_expr.appendleft(str(res))

print(res)
