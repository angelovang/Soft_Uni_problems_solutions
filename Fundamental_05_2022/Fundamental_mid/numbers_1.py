from typing import List

sequence_of_integers: list[int] = list(map(int, input().split()))

average = sum(sequence_of_integers) / len(sequence_of_integers)
sequence_of_integers = sorted(sequence_of_integers, reverse=True)
result = []

for x in sequence_of_integers:
    if x > average and len(result) < 5:
        result.append(x)
    else:
        break

if len(result) == 0:
    print(f'No')
else:
    print(*result)
