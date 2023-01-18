people_queue = int(input())
lift_wagon = [int(x) for x in input().split(' ')]

lift_is_full = False
queue_is_empty = False

for i in range(len(lift_wagon)):
    while lift_wagon[i] <4 and people_queue >0 :
        lift_wagon[i] += 1
        people_queue -= 1
    if lift_wagon[-1] == 4:
        lift_is_full = True
    if people_queue == 0:
        queue_is_empty = True
        break

if queue_is_empty and not lift_is_full:
    print(f'The lift has empty spots!')
    print(*lift_wagon)
elif not queue_is_empty and lift_is_full:
    print(f"There isn't enough space! {people_queue} people in a queue!")
    print(*lift_wagon)
else:
    print(*lift_wagon)

