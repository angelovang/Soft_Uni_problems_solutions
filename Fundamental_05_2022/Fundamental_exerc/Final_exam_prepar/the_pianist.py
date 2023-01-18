def colect_info(number_of_pieces_,pieces_dict_):
    for i in range(number_of_pieces_):
        info = input().split('|')
        piece = info[0]
        composer = info[1]
        key = info[2]
        if piece not in pieces_dict_:
            pieces_dict_[piece] = [composer , key]
    return pieces_dict_

##############################

def organize_info(pieces_dict_):
    while True:
        command = input().split('|')
        if command[0] == 'Stop':
            break

        elif command[0] == 'Add':
            piece = command[1]
            composer = command[2]
            key = command[3]
            if piece not in pieces_dict_:
                pieces_dict_[piece] = [composer, key]
                print(f'{piece} by {composer} in {key} added to the collection!')
            else:
                print(f'{piece} is already in the collection!')

        elif command[0] == 'Remove':
            piece = command[1]
            if piece in pieces_dict_:
                pieces_dict_.pop(piece)
                print(f'Successfully removed {piece}!')
            else:
                print(f'Invalid operation! {piece} does not exist in the collection.')

        elif command[0] == 'ChangeKey':
            piece = command[1]
            new_key = command[2]
            if piece in pieces_dict_:
                pieces_dict_[piece][1] = new_key
                print(f'Changed the key of {piece} to {new_key}!')
            else:
                print(f'Invalid operation! {piece} does not exist in the collection.')

    return pieces_dict_

###############################

def print_info(pieces_dict_):
    for piece in pieces_dict_:
        print(f'{piece} -> Composer: {pieces_dict_[piece][0]}, Key: {pieces_dict_[piece][1]}')
    return

number_of_pieces = int(input())
pieces_dict = {}
pieces_dict = colect_info(number_of_pieces,pieces_dict)
pieces_dict = organize_info(pieces_dict)
print_info(pieces_dict)

