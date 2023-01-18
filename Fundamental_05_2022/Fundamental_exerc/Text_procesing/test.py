text = input()
text = text.replace(' ', '')
text = text.split(',')
#text = [x for x in text if x != '']

lenght = len(text)
win = False
win_symbol = ''
win_lenght = 0
jackpot = False


def check_winning(smbl, l, r):
    win_ = False
    win_symbol_ = ''
    win_lenght_ = 0
    jackpot_ = False
    for i in range(10, 5, -1):
        if smbl * i in l and smbl * i in r:
            win_ = True
            win_symbol_ = smbl
            win_lenght_ = i
            if i == 10:
                jackpot_ = True
            return win_, win_symbol_, win_lenght_, jackpot_
    win_ = False
    win_symbol_ = ''
    win_lenght_ = 0
    jackpot_ = False
    return win_, win_symbol_, win_lenght_, jackpot_


for ticket in text:
    if len(ticket) != 20 :
        print(f'invalid ticket')
    else:
        left_side = ticket[0:10]
        right_side = ticket[10:20]
        for symbol in left_side:
            if symbol == '@' or symbol == '#' or symbol == '$' or symbol == '^':
                win, win_symbol, win_lenght, jackpot = check_winning(symbol, left_side, right_side)
                if win:
                    break
        if win:
            if jackpot:
                print(f'ticket "{ticket}" - {win_lenght}{win_symbol} Jackpot!')
            else:
                print(f'ticket "{ticket}" - {win_lenght}{win_symbol}')
        else:
            print(f'ticket "{ticket}" - no match')
if lenght == 0:
    print(f'invalid ticket')
