first_list = input().split(', ')
second_list = input().split(', ')
new_list = []

for str_1 in first_list:
    for str_2 in second_list:
        if str_1 in str_2 :
            new_list.append(str_1)
            break
print(new_list)
