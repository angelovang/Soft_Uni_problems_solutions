str_1 , str_2 = input().split(' ')
str_3 = ''
sum = l = 0

if len(str_1) > len(str_2):
    str_3 += str_1[len(str_2):]
    l = len(str_2)
else:
    str_3 += str_2[len(str_1):]
    l = len(str_1)

for i in range(l):
    sum += ord(str_1[i])*ord(str_2[i])
for ch in str_3:
    sum += ord(ch)

print(sum)
