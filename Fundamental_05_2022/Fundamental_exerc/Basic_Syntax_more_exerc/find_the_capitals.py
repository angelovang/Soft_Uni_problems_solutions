single_string = input()
index_list = []

for i in range(len(single_string)):
    if 65 <= ord(single_string[i]) <= 90 :
        index_list.append(i)
print(index_list)
