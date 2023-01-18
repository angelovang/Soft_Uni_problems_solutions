a =  list(map(int,input().split(' ')))
b =  list(map(int,input().split(' ')))
c =  list(map(int,input().split(' ')))

first_pl_won = False
second_pl_won = False

if a.count(1) == 3 or b.count(1) == 3 or c.count(1) == 3 \
        or a[0]==b[0]==c[0]==1 or a[-1]==b[-1]==c[-1]==1 \
        or a[1]==b[1]==c[1]==1 or a[0]==b[1]==c[-1]==1 \
        or a[2]==b[1]==c[0]==1:
    first_pl_won = True
    print(f'First player won')

elif a.count(2) == 3 or b.count(2) == 3 or c.count(2) == 3 \
        or a[0]==b[0]==c[0]==2 or a[-1]==b[-1]==c[-1]==2 \
        or a[1]==b[1]==c[1]==2 or a[0]==b[1]==c[-1]==2 \
        or a[2]==b[1]==c[0]==2:
    first_pl_won = True
    print(f'Second player won')
else:
    print(f'Draw!')



