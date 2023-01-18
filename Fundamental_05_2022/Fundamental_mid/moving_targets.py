targets_list = [int(x) for x in input().split()]
result_array = []


def shoot(array , comm):
    index = int(comm[1])
    power = int(comm[2])
    index_is_valid = 0 <= index <= (len(array) - 1)
    if index_is_valid:
        array[index] -= power
        if array[index] <= 0 :
            array.pop(index)
    else:
        pass
    return array


def add(array, comm):
    index = int(comm[1])
    value = int(comm[2])
    index_is_valid = 0 <= index <= (len(array) - 1)
    if index_is_valid:
        array.insert(index, value)
    else:
        print(f"Invalid placement!")
    return array


def strike(array, comm):
    index = int(comm[1])
    radius = int(comm[2])
    index_is_valid = (0 <= index - radius) and (index + radius <= len(array) - 1)
    if index_is_valid:
        result_arr = [array[i] for i in range(len(array)) if (i < index - radius) or (i > index + radius)]
        return result_arr
    else:
        print(f"Strike missed!")
        return array


while True:
    command = input()
    if command == 'End':
        break
    else:
        command = command.split()
        if command[0] == 'Shoot':
            targets_list = shoot(targets_list, command)
        elif command[0] == 'Add':
            targets_list = add(targets_list, command)
        elif command[0] == 'Strike':
            targets_list = strike(targets_list, command)

# noinspection PyUnboundLocalVariable
print('|'.join(map(str, targets_list)))
