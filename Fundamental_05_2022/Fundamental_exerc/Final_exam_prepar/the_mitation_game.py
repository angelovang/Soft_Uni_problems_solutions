message = input()

while True:
    command = input().split('|')
    if command[0] == 'Decode':
        print(f'The decrypted message is: {message}')
        break
    current_command = command[0]
    if current_command == 'Move':
        numbers_of_letters = int(command[1])
        for i in range(numbers_of_letters):
            ch = message[0]
            message = message[1:] + ch
    elif current_command == 'Insert':
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]
    elif current_command == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring,replacement)
