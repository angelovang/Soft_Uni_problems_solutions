initial_treasure = [x for x in input().split('|')]
print(initial_treasure)
end_treasure = initial_treasure.copy()


def loot(arr,comm):
    items = comm.pop[0]
    for item in items:
        if item not in arr :
            arr = arr.insert(0)
    return arr


def drop(arr,index):
    i = int(index[1])
    if 0 <= i <= len(arr)-1 :
        a = arr.pop(i)
        arr = arr.append(a)
    return arr


def steal(arr,count):
    cnt = int(count[1])
    return arr


while True :
    command = input()
    if command == 'Yohoho!' :
        break
    else:
        command = command.split()
        cmd = command[0]
        if cmd == 'Loot' :
            end_treasure = loot(end_treasure,command)
        elif cmd == 'Drop' :
            end_treasure = drop(end_treasure,command)
        elif cmd == 'Steal' :
            end_treasure = steal(end_treasure,command)

sum = 0
ll = len(end_treasure)
if len == 0 :
    print(f'Failed treasure hunt.')
else:
    for i in range(ll):
        sum += len(end_treasure[i])
    average_gain = sum / ll
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')