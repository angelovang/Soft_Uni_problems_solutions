zoo = {}
l_area = {}

while True:
    command = input()
    if command == 'EndDay':
        break
    else:
        command = command.split(' ')
        cmd = command[0]
        info = command[1].split('-')

        if cmd == 'Add:' :
            name = info[0]
            needet_food = int(info[1])
            area = info[2]
            if name not in zoo :
                zoo[name] = {'food': needet_food, 'area': area }
                if area not in l_area:
                    l_area[area] = 1
                else:
                    l_area[area] += 1
            else:
                zoo[name]['food'] += needet_food
 #               l_area[area] += 1


        elif cmd == 'Feed:':
            name = info[0]
            feedet_food = int(info[1])
            if name not in zoo:
                continue
            else:
                zoo[name]['food'] -= feedet_food
                if zoo[name]['food'] <= 0 :
                    area = zoo[name]['area']
                    zoo.pop(name)
                    l_area[area] -= 1
                    print(f'{name} was successfully fed')


#print(zoo)
#print(l_area)

print(f'Animals:')
for name in zoo:
    print(f"{name} -> {zoo[name]['food']}g")

print(f'Areas with hungry animals:')
for area,count in l_area.items():
    if count > 0 :
        print(f'{area}: {count}')

