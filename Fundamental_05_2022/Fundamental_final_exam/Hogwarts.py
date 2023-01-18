text = input()

while True:
    command = input().split(' ')
    if command[0] == 'Abracadabra':
        break

    comm = command[0]

    if comm == 'Abjuration':
        text = text.upper()
        print(text)

    elif comm == 'Necromancy':
        text = text.lower()
        print(text)

    elif comm == 'Illusion':
        index = int(command[1])
        letter = command[2]
        if 0 <= index < len(text) :
            text = text[:index] + letter + text[index+1:]
            print('Done!')
        else :
            print(f'The spell was too weak.')

    elif comm == 'Divination':
        first_substr = command[1]
        second_substr = command[2]
        if first_substr in text:
            text = text.replace(first_substr,second_substr)
            print(text)

    elif comm == 'Alteration' :
        substr = command[1]
        if substr in text :
            text = text.replace(substr,'')
            print(text)

    else:
        print(f'The spell did not work!')

