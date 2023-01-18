name = ''
gools = 0
best_player = ''
temp_gools = 0
hat_trick = 3

while gools < 10 :
    name = input()
    if name == "END":
        break
    gools = int(input())
    if gools > temp_gools :
        best_player = name
        temp_gools = gools

print(f'{best_player} is the best player!')
if temp_gools >= hat_trick :
    print(f'He has scored {temp_gools} goals and made a hat-trick !!!')
else:
    print(f'He has scored {temp_gools} goals.')

