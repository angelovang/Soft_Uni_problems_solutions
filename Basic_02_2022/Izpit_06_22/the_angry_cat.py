items = [int(x) for x in input().split(', ')]
entry_point = int(input())
type_of_items = input()


def sum_damage(arr,type):
    sum = 0
    if type == 'cheap':
        for a in arr :
            if a < items[entry_point]:
                sum += a
    else:
        for a in arr :
            if a >= items[entry_point]:
                sum += a
    return sum

left_items = [items[i] for i in range(len(items)) if i < entry_point ]
right_items = [items[j] for j in range(len(items)) if j > entry_point ]

left_sum = sum_damage(left_items,type_of_items)
right_sum = sum_damage(right_items,type_of_items)

if left_sum >= right_sum:
    position = 'Left'
    sum_rating = left_sum
else:
    position = 'Right'
    sum_rating = right_sum
print(f'{position} - {sum_rating}')


