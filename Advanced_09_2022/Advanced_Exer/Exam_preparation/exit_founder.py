players = list(input().split(', '))

Size = 6
board = []
rest = {'Tom': 'play', 'Jerry': 'play'}
for row in range(Size):
    board.append(input().split())

while True:
    current_pos = list(map(int, input().strip('()').split(', ')))
    value = board[current_pos[0]][current_pos[1]]

    player = players[0]
    if rest[player] == 'rest':
        rest[player] = 'play'
        players[0], players[-1] = players[-1], players[0]
        continue

    if value == 'E':
        print(f'{player} found the Exit and wins the game!')
        break

    if value == 'T':
        print(f'{player} is out of the game! The winner is {players[1]}.')
        break

    if value == 'W':
        print(f'{players[0]} hits a wall and needs to rest.')
        rest[players[0]] = 'rest'

    players[0], players[-1] = players[-1], players[0]

