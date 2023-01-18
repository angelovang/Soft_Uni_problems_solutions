element_list = [x for x in input().split()]
moves_counter = 0



while True and (len(element_list) != 0) :
    command = input()
    if command == 'end':
        break
    else:
        moves_counter += 1
        comm_as_index = list(map(int,command.split()))
        first_index = comm_as_index[0]
        second_index = comm_as_index[1]

        if first_index == second_index or \
            first_index < 0 or first_index >= len(element_list) or \
            second_index < 0 or second_index >= len(element_list) :
            i = int(len(element_list )/ 2)
            element_list.insert(i,f'-{moves_counter}a')
            element_list.insert(i,f'-{moves_counter}a')
            print(f'Invalid input! Adding additional elements to the board')

        else:
            if element_list[first_index] != element_list[second_index]:
                print(f'Try again!')
            else:
                current_element = element_list[first_index]
                print(f'Congrats! You have found matching elements - {current_element}!')
                element_list.remove(current_element)
                element_list.remove(current_element)

if len(element_list) == 0 :
    print(f'You have won in {moves_counter} turns!')
else:
    print(f'Sorry you lose :(')
    print(*element_list)


