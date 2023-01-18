start_array = input().split()
current_array = start_array.copy()


def merge_string(array, command_string):
    len_list = len(array) - 1
    w_arr = array.copy()
    start_index = abs(int(command_string[1]))
    if start_index > len_list:
        return array

    end_index = abs(int(command_string[2]))
    if end_index > len_list:
        end_index = -1
    work_string = ''

    for i in range(start_index,end_index):
        work_string += array[i]
        w_arr.pop(i)


    w_arr.insert(start_index,work_string)
    return w_arr




def divide_string(array,command_string):
    pass


while True :
    command = input().split()
    if command[0] == '3:1':
        break
    elif command[0] == 'merge':
        end_ar = merge_string(current_array,command)
    elif command[0] == 'divide' :
        divide_string(current_array,command)

print(" ".join(end_ar))


