initial_list = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        print(', '.join(initial_list))
        break
    else:
        comm = command.split()
        action = comm[0]
        item = comm[1]
        if action == 'Urgent':
            if item not in initial_list:
                initial_list.insert(0,item)
        elif action == 'Unnecessary':
            if item in initial_list:
                initial_list.remove(item)
        elif action == 'Correct':
            if item in initial_list:
                i = initial_list.index(item)
                initial_list[i] = comm[2]
        elif action == 'Rearrange':
            if item in initial_list:
                initial_list.remove(item)
                initial_list.append(item)


