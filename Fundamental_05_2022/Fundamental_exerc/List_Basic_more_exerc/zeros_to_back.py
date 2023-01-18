single_string = input().split(', ')

for i in range(len(single_string)-1,-1,-1):
    single_string[i] = int(single_string[i])
    if int(single_string[i]) ==  0:
        a = single_string.pop(i)
        single_string.append(a)
print(single_string)
