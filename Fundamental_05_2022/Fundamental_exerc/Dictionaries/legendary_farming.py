materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
legendary_item = ''


def analise_data(current_data):
    legendary = None
    for i in range(0, len(current_data), 2):
        quantity, material = int(current_line[i]), current_line[i + 1]
        material = material.lower()
        if material not in materials:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity
        else:
            materials[material] += quantity
            if materials[material] >= 250:
                materials[material] -= 250
                if material == 'shards':
                    legendary = 'Shadowmourne'
                elif material == 'fragments':
                    legendary = 'Valanyr'
                elif material == 'motes':
                    legendary = 'Dragonwrath'
                return legendary


while True:
    current_line = input().split()
    legendary_item = analise_data(current_line)
    if legendary_item != None:
        break
print(f'{legendary_item} obtained!')
for m in materials:
    print(f'{m}: {materials[m]}')
for j in junk:
    print(f'{j}: {junk[j]}')

