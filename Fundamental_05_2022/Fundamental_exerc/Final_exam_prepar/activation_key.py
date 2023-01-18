activation_key = input()

while True:
    command = input().split('>>>')
    if command[0] == 'Generate':
        break
    else:
        instruction = command[0]

        if instruction == 'Contains':
            substring = command[1]
            if substring in activation_key:
                print(f'{activation_key} contains {substring}')
            else:
                print(f'Substring not found!')

        elif instruction == 'Flip':
            case = command[1]
            start_index = int(command[2])
            end_index = int(command[3])

            if case == 'Lower':
                current_string = activation_key[start_index:end_index].lower()
            else:
                current_string = activation_key[start_index:end_index].upper()

            activation_key = activation_key[:start_index]+current_string+activation_key[end_index:]
            print(activation_key)

        elif instruction == 'Slice':
            start_index =int(command[1])
            end_index = int(command[2])
            activation_key = activation_key[:start_index] + activation_key[end_index:]
            print(activation_key)

print(f'Your activation key is: {activation_key}')

