neighborhood = [int(x) for x in input().split('@')]
index = 0


def cupid(arr,x):
    if arr[x] == 0:
        print(f"Place {x} already had Valentine's day.")
    else:
        arr[x] -= 2
        if arr[x] == 0:
            print(f"Place {x} has Valentine's day.")
    return arr


while True :
    command = input()
    if command == 'Love!':
        break
    else:
        cmd = command.split()
        action = cmd[0]
        step = int(cmd[1])
        if action == 'Jump':
            index += step
            if index >= len(neighborhood):
                index = 0
            neighborhood = cupid(neighborhood,index)

end_sum = sum(neighborhood)
failed_houses = len(neighborhood) - neighborhood.count(0)

print(f"Cupid's last position was {index}.")
if end_sum == 0:
    print(f'Mission was successful.')
else:
    print(f'Cupid has failed {failed_houses} places.')

