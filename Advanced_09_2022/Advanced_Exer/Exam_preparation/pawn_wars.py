chess_board = []
chess_board_index = [
    ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
    ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
    ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
    ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
    ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
    ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
    ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
    ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
    ]
w_pos = []
b_pos = []
end_game = False


def w_move(pos) :
    r = pos[0]-1
    c = pos[1]
#    print(r,c,'w')
    chess_board[r+1][c] = '-'

    if c > 0 and chess_board[r][c-1] == 'b' :
        print(f'Game over! White win, capture on {chess_board_index[r][c-1]}.')
        return True

    if c < 7 and chess_board[r][c+1] == 'b' :
        print(f'Game over! White win, capture on {chess_board_index[r][c+1]}.')
        return True

    if r == 0:
        print(f'Game over! White pawn is promoted to a queen at {chess_board_index[r][c]}.')
        return True
    w_pos[0] = r
    chess_board[r][c] = 'w'
    return False


def b_move(pos) :
    r = pos[0]
    c = pos[1]
#    print(r,c,'b')
    chess_board[r][c] = '-'
    if c > 0 and chess_board[r+1][c-1] == 'w':
        print(f'Game over! Black win, capture on {chess_board_index[r+1][c-1]}.')
        return True
    if c < 7 and chess_board[r+1][c+1] == 'w':
        print(f'Game over! Black win, capture on {chess_board_index[r+1][c+1]}.')
        return True
    r += 1
    if r == 7:
        print(f'Game over! Black pawn is promoted to a queen at {chess_board_index[r][c]}.')
        return True
    b_pos[0] = r
    chess_board[r][c] = 'b'
    return False


for row in range(8):
    chess_board.append(input().split())
    if 'w' in chess_board[row] :
        w_pos = [row,chess_board[row].index('w')]

    if 'b' in chess_board[row] :
        b_pos = [row,chess_board[row].index('b')]
#    print(chess_board[row])

while True:

    end_game = w_move(w_pos)
    if end_game :
        break

    end_game = b_move(b_pos)
    if end_game :
        break

