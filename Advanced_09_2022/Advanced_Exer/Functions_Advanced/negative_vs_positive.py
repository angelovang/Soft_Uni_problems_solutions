def neg_pos_sum(*arg):
    neg_sum = 0
    pos_sum = 0
    for n in arg:
        if n > 0:
            pos_sum += n
        else:
            neg_sum += n
    return neg_sum, pos_sum


numbers = list(map(int, input().split()))
neg,pos = neg_pos_sum(*numbers)
print(neg)
print(pos)
if abs(neg) > pos:
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')

