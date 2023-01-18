lines = int(input())
table = set()
line = []
for _ in range(lines):
    line = input().split()
    for ch in line:
        table.add(ch)

for element in table:
    print(element)
