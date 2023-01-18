from collections import deque

elv_energy = deque(map(int, input().split()))
boxes = list(map(int, input().split()))

total_number_of_toy = 0
total_used_energy = 0
counter = 0

while elv_energy and boxes:
    #    print(counter ,' - ',total_number_of_toy,' - ', total_used_energy)
    counter += 1
    elv = elv_energy.popleft()
    box = boxes[-1]

    if elv < 5:
        continue

    elif elv < box:
        elv_energy.append(elv * 2)
        continue

    else:
        if counter % 3 == 0:
            if elv >= 2 * box:
                box = boxes.pop()
                total_used_energy += 2 * box

                if counter % 5 != 0:
                    total_number_of_toy += 2
                    elv = elv - 2 * box + 1
                else:
                    elv = elv - 2 * box

                elv_energy.append(elv)

            else: # drink chocolate
                elv_energy.append(elv * 2)

        else:  # counter != 3
            box = boxes.pop()
            total_used_energy += box

            if counter % 5 != 0:
                total_number_of_toy += 1
                elv = elv - box + 1
            else:
                elv -= box

            elv_energy.append(elv)

print(f'Toys: {total_number_of_toy}')
print(f'Energy: {total_used_energy}')
if elv_energy:
    print(f'Elves left: {", ".join(map(str, elv_energy))}')
if boxes:
    print(f'Boxes left: {", ".join(map(str, boxes))}')
