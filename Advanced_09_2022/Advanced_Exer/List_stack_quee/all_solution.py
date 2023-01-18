#01. Reverse Numbers

numbers = list(map(int, input().split()))
for _ in range(len(numbers)):
    removed_element = numbers.pop()
    print(removed_element, end=" ")

#=======================================================================================================================================

#02. Stacked Queries

my_stack = []
n = int(input())

for _ in range(n):
    current_input = [int(x) for x in input().split()]
    if len(current_input) > 1:
        current_num = current_input[1]
        my_stack.append(current_num)
    else:
        type_num = current_input[0]
        if type_num == 2 and my_stack:
            my_stack.pop()

        elif type_num == 3 and my_stack:
            print(max(my_stack))

        elif type_num == 4 and my_stack:
            print(min(my_stack))

final_print_stack = []
for _ in range(len(my_stack)):
    popped_el = my_stack.pop()
    final_print_stack.append(popped_el)

print(*final_print_stack, sep=', ')

#=======================================================================================================================================

#03. Fast Food


from collections import deque

total_food = int(input())
all_orders = deque([int(x) for x in input().split()])

biggest_order = max(all_orders)
print(biggest_order)

while all_orders:
    completed = False
    for order in all_orders:
        if total_food >= order:
            all_orders.popleft()
            total_food -= order
            break
        else:
            completed = True
            break

    if completed:
        break

if not all_orders:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join([str(x) for x in all_orders])}')

#=======================================================================================================================================

#04. Fashion Boutique

clothes_stack = [int(x) for x in input().split()]
default_cap = int(input())
rack_cap = default_cap
count_racks = 1
while clothes_stack:
    last_cloth = clothes_stack[-1]
    if last_cloth <= rack_cap:
        rack_cap -= last_cloth
        clothes_stack.pop()
    else:
        rack_cap = default_cap
        count_racks += 1

print(count_racks)

#=======================================================================================================================================

#05. Truck Tour


from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    pump_details = [int(x) for x in input().split()]
    pumps.append(pump_details)

for starts in range(n):
    tank = 0
    failed = False

    for details in pumps:
        fuel = details[0]
        kms = details[1]
        tank += fuel
        if kms > tank:
            failed = True
            break
        else:
            tank -= kms

    if failed:
        removed = pumps.popleft()
        pumps.append(removed)
    else:
        print(starts)
        break

#=======================================================================================================================================

#06. Balanced Parentheses

sequence = input()
balanced = False
brackets = []

for el in sequence:
    if el in '({[':
        brackets.append(el)
    elif el in ')}]' and brackets:
        popped_last = brackets.pop()
        if popped_last + el in '()[]{}':
            balanced = True
        else:
            balanced = False
            break
    else:
        balanced = False
        break

if balanced and not brackets:
    print('YES')
else:
    print('NO')

#=======================================================================================================================================

#07. Robotics

from collections import deque


def convert_str_to_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(':')]
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_seconds_to_str_time(seconds):
    seconds %= 24 * 60 * 60

    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots_data = input().split(';')
process_time_by_robot = {}
busy_until_by_robot = {}

for robot_data in robots_data:
    name, process_time = robot_data.split('-')
    process_time_by_robot[name] = int(process_time)
    busy_until_by_robot[name] = -1

time = convert_str_to_seconds(input())
items = deque()

while True:
    line = input()
    if line == 'End':
        break
    items.append(line)

while items:
    time = (time + 1)
    item = items.popleft()

    for name, busy_until in busy_until_by_robot.items():
        if time >= busy_until:
            busy_until_by_robot[name] = time + process_time_by_robot[name]
            print(f'{name} - {item} [{convert_seconds_to_str_time(time)}]')
            break
    else:
        items.append(item)

#=======================================================================================================================================

#08. Crossroads

from collections import deque

green_light = int(input())
window = int(input())

cars = deque()
cars_counter = 0
crashed = False

command = input()

while command != "END":
    if command == "green":
        if cars:
            current = cars.popleft()
            seconds_left = green_light - len(current)
            while seconds_left > 0:
                cars_counter += 1
                if cars:
                    current = cars.popleft()
                    seconds_left -= len(current)
                else:
                    break
            if seconds_left == 0:
                cars_counter += 1
            if window >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                idx = window + seconds_left
                print("A crash happened!")
                print(f"{current} was hit at {current[idx]}.")
                crashed = True
                break
    else:
        cars.append(command)
    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")

#=======================================================================================================================================

#09. Key Revolver

from collections import deque

bullet_price = int(input())
size_barrel = int(input())

bullets = input().split(' ')
bullets = deque([int(item) for item in bullets])

org_bullets = deque(bullets)

locks = input().split(' ')
locks = deque([int(item) for item in locks])

intelligence = int(input())
shoot = 0

while bullets and locks:
    if bullets and shoot == size_barrel:
        print(f'Reloading!')
        shoot = 0
    if bullets[-1] <= locks[0]:
        print('Bang!')
        bullets.pop()
        locks.popleft()
        shoot += 1
    else:
        print('Ping!')
        bullets.pop()
        shoot += 1

if bullets and shoot == size_barrel:
    print(f'Reloading!')
    shoot = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    cost = (len(org_bullets) - len(bullets)) * bullet_price
    profit = intelligence - cost
    print(f"{len(bullets)} bullets left. Earned ${profit}")

#=======================================================================================================================================

#10. Cups and Bottles

from collections import deque

cups = deque(int(x) for x in input().split())
bottles = list(int(x) for x in input().split())

wasted_water = 0

while True:
    if cups and bottles:
        current_cup = cups.popleft()
        current_bottle = bottles.pop()
        if current_bottle >= current_cup:
            wasted_water += current_bottle - current_cup
        else:
            cups.appendleft(current_cup - current_bottle)
    else:
        break

if cups:
    result = ' '.join([str(x) for x in cups])
    print(f"Cups: {result}")
if bottles:
    res = ' '.join([str(x) for x in bottles])
    print(f"Bottles: {res}")

print(f"Wasted litters of water: {wasted_water}")

#=======================================================================================================================================