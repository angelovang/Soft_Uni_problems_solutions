from collections import deque
quantity_water = int(input())
people_names = deque()

while True:
    current_name = input()
    if current_name == 'Start':
        break
    else:
        people_names.append(current_name)

while True:
    command = input().split()
    if command[0] == 'End':
        print(f'{quantity_water} liters left')
        break
    elif command[0] == 'refill':
        quantity_water += int(command[1])
    else:
        litters = int(command[0])
        person_name = people_names.popleft()
        if litters > quantity_water:
            print(f'{person_name} must wait')
        else:
            quantity_water -= litters
            print(f'{person_name} got water')

