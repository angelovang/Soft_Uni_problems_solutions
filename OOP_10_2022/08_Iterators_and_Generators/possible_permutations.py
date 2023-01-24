from itertools import permutations


def possible_permutations(inp_list: list):
    for perm in permutations(inp_list):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
print()
print()
[print(n) for n in possible_permutations([1])]
