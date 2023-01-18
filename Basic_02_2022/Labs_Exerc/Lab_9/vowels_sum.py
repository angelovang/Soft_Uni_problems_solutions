word = input()

sum_vovel = 0
for ch in word :
    if ch == 'a':
        sum_vovel += 1
    elif ch == 'e':
        sum_vovel += 2
    elif ch == 'i':
        sum_vovel += 3
    elif ch == 'o':
        sum_vovel += 4
    elif ch == 'u':
        sum_vovel += 5

print(sum_vovel)
