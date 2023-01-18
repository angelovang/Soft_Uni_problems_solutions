start_list = list(map(int,input().split(' ')))
step = int(input())
counter = len(start_list)
index = 0
end_list = []

while counter > 0 :
    index += step - 1
    if index >= len(start_list):
        while index >= len(start_list):
            index = index - len(start_list)
    end_list.append(start_list.pop(index))
    counter -= 1

print('[',end='')
print(*end_list,sep=',',end='')
print(']')

