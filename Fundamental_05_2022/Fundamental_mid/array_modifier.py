initial_array = [int(x) for x in input().split()]


def swap(array,comm):
    i = int(comm[1])
    j = int(comm[2])
    a = array[i]
    array[i] = array[j]
    array[j] = a
    return array


def multiply(array,comm):
    i = int(comm[1])
    j = int(comm[2])
    a = array[i] * array[j]
    array[i] = a
    return array


def decrease(array):
    array = [(x-1) for x in array]
    return array


while True:
    command = input()
    if command == 'end':
        break
    else:
        command = command.split()
        if command[0] == 'swap':
            initial_array = swap(initial_array, command)
        elif command[0] == 'multiply':
            initial_array = multiply(initial_array, command)
        elif command[0] == 'decrease':
            initial_array = decrease(initial_array)


print(', '.join(map(str, initial_array)))

