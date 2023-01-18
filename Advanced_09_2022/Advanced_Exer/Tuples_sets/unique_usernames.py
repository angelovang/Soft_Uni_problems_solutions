lines = int(input())
names = set()
for _ in range(lines):
    name = input()
    names.add(name)

for name in names:
    print(name)
