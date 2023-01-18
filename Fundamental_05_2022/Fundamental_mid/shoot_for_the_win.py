target_list = [int(x) for x in input().split()]
count = 0

while True :
    command = input()
    if command == 'End':
        break
    else:
        i = int(command)
        if 0 <= i <= (len(target_list)-1):
            if target_list[i] != -1:
                target = target_list[i]
                target_list[i] = -1
                count += 1
                for j in range(len(target_list)):
                    if target_list[j] != -1:
                        if target_list[j] <= target:
                            target_list[j] += target
                        else:
                            target_list[j] -= target


print(f"Shot targets: {count} ->",*target_list)

