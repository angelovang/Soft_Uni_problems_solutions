n , m = (map(int,input().split()))

a = set()
b = set()

for _ in range(n):
    num = input()
    a.add(num)
for _ in range(m):
    num = input()
    b.add(num)
c = a.intersection(b)
for x in c:
    print(x)
