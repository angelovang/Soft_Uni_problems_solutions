lines = int(input())
longest_intersection = []
set_1 = set()
set_2 = set()
for _ in range(lines):
    ranges = input().split('-')
    limits = [tuple(map(int,l.split(','))) for l in ranges]
    set_1 = set(n for n in range(limits[0][0],limits[0][1]+1))
    set_2 = set(m for m in range(limits[1][0], limits[1][1]+1))
    result = set_1.intersection(set_2)
    if len(longest_intersection) < len(result):
        longest_intersection = result
print(f"Longest intersection is [{', '.join(map(str,longest_intersection))}] with length {len(longest_intersection)}")

