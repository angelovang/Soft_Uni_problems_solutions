from collections import deque
from typing import List

materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

# print(materials)
# print(magic_level)

gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0,
}
made_gifts = []
successed = False
gift = ''

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    needed_sum = material + magic

    if needed_sum < 100:
        if needed_sum % 2 == 0:
            needed_sum = material * 2 + magic * 3
        else:
            needed_sum = needed_sum * 2

    elif needed_sum > 499:
        needed_sum = needed_sum / 2

    if 100 <= needed_sum < 500:
        if 100 <= needed_sum < 200 :
            gift = 'Gemstone'
        elif 200 <= needed_sum < 300 :
            gift = 'Porcelain Sculpture'
        elif 300 <= needed_sum < 400 :
            gift = 'Gold'
        elif 400 <= needed_sum < 500 :
            gift = 'Diamond Jewellery'

        gifts[gift] += 1
        if gift not in made_gifts:
            made_gifts.append(gift)
    else:
        continue

if 'Gemstone' in made_gifts and 'Porcelain Sculpture' in made_gifts :
    successed = True
elif 'Gold' in made_gifts and 'Diamond Jewellery' in made_gifts :
    successed = True

if successed :
    print(f"The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")

if materials :
    print(f"Materials left: {', '.join(map(str,materials))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str,magic_level))}")

#made_gifts = list(set(made_gifts))
for name in sorted(made_gifts):
    print(f"{name}: {gifts[name]}")
