gift_list = input().split()
command = ''
command_list = []
while command != 'No Money':
    command = input()
    command_list = command.split()
#    print(command_list)
    if command_list[0] == 'OutOfStock':
        while command_list[1] in gift_list:
            ind = gift_list.index(command_list[1])
            gift_list[ind] = 'None'
    elif command_list[0] == 'Required':
        if 0 <= int(command_list[2]) < len(gift_list):
            gift_list[int(command_list[2])] = command_list[1]
    elif command_list[0] == 'JustInCase':
        gift_list[-1] = command_list[1]
    else:
        pass
for element in gift_list:
    if element != 'None':
        print(element,end=' ')
