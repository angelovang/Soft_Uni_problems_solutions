text = input()
text = text.replace(' ','')
text = text.split(',')
#text = [x for x in text if x != '']

lenght = len(text)
win = False
win_symbol = ''
win_lenght = 0
jackpot = False

def check_winning(smbl, l, r):
    if smbl * 10 in l and smbl * 10 in r:
        win = True
        win_symbol = smbl
        win_lenght = 10
        jackpot = True
        return win , win_symbol , win_lenght, jackpot
    elif smbl * 9 in l and smbl * 9 in r:
        win = True
        win_symbol = smbl
        win_lenght = 9
        jackpot = False
        return win, win_symbol, win_lenght, jackpot
    elif smbl * 8 in l and smbl * 8 in r:
        win = True
        win_symbol = smbl
        win_lenght = 8
        jackpot = False
        return win, win_symbol, win_lenght, jackpot
    elif smbl * 7 in l and smbl * 7 in r:
        win = True
        win_symbol = smbl
        win_lenght = 7
        jackpot = False
        return win, win_symbol, win_lenght, jackpot
    elif smbl * 6 in l and smbl * 6 in r:
        win = True
        win_symbol = smbl
        win_lenght = 6
        jackpot = False
        return win, win_symbol, win_lenght , jackpot
    else:
        win = False
        win_symbol = ''
        win_lenght = 0
        jackpot = False
        return win, win_symbol, win_lenght, jackpot


for ticket in text:
    if len(ticket) != 20:
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
