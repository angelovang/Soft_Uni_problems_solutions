from collections import deque

materials_in_box = list(int(mat) for mat in input().split())
magic_levels = deque(int(mag) for mag in input().split())

table_recipe = {
    'Doll' : 150,
    'Wooden train' : 250,
    'Teddy bear' : 300,
    'Bicycle' : 400
    }

total_magic_level = 0
crafted_presents = {}

while materials_in_box and magic_levels:
    material = materials_in_box[-1]
    magic = magic_levels[0]
    is_equal = False

    if magic == 0 or material == 0 :
        if magic == 0 :
            magic_levels.popleft()

        if material == 0 :
            materials_in_box.pop()
        continue

    current_magic = magic * material

    if current_magic < 0:
        materials_in_box.append(materials_in_box.pop() + magic_levels.popleft())

    for present , m_needet in table_recipe.items():
        if current_magic == m_needet:
            if present not in crafted_presents:
                crafted_presents[present] = 0
            crafted_presents[present] += 1
            materials_in_box.pop()
            magic_levels.popleft()
            is_equal = True
            break

    if is_equal == False and current_magic >= 0:
        magic_levels.popleft()
        materials_in_box[-1] += 15

if ('Doll' in crafted_presents and 'Wooden train' in crafted_presents) or \
        ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents) :
    print(f'The presents are crafted! Merry Christmas!')
else:
    print(f'No presents this Christmas!')

if materials_in_box:
    print(f"Materials left: {', '.join(map(str,materials_in_box[::-1]))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str,magic_levels))}")

for name in sorted(crafted_presents) :
    print(f'{name}: {crafted_presents[name]}')



