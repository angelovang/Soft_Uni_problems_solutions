a = int(input())
b = int(input())
c = int(input())

positive = (a>0 and b>0 and c>0) or (a>0 and b<0 and c<0) or (b>0 and a<0 and c<0) or (c>0 and b<0 and a<0)

if a == 0 or b == 0 or c ==0 :
    print('zero')
elif positive :
    print('positive')
else:
    print('negative')

