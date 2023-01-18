row , col = map(int,input().split())

def make_string(x,y):
    first_ch = chr(x+97)
    second_ch = chr(x+y+97)
    txt = first_ch + second_ch + first_ch
    return txt

for i in range(row):
    for j in range(col):
        print(make_string(i,j), end=' ')
    print()
