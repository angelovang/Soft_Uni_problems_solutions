concealed_message = input()
message = concealed_message
while True:
    command = input().split(':|:')
    if command[0] == 'Reveal':
        break
    elif command[0] == 'InsertSpace' :
        index = int(command[1])
        single_space = ' '
        message = message[:index] + single_space + message[index:]
        print(message)

    elif command[0] == 'Reverse' :
        substring = command[1]
        if substring in message:
            current_str = message.partition(substring)
            message = current_str[0] + current_str[2] + current_str[1][::-1]
            print(message)
        else:
            print('error')
    elif command[0] == 'ChangeAll' :
        substring = command[1]
        replasement = command[2]
        message = message.replace(substring,replasement)
        print(message)

print(f'You have a new text message: {message}')

