from math import ceil
sequence_of_numbers = [int(x) for x in input().split(', ')]
current_sequence = sequence_of_numbers.copy()
group = 10 * ceil( max(sequence_of_numbers) / 10)
group_1 = 0
list_of_numbers = []
for gr in range(10,group+1,10) :
    for num in sequence_of_numbers:
        if group_1 < num <= gr:
            list_of_numbers.append(num)

    print(f"Group of {gr}'s: {list_of_numbers}")
    list_of_numbers = []
    group_1 += 10




