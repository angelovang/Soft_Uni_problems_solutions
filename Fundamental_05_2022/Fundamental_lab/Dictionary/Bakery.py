table_list = [x for x in input().split(' ')]
table_dict = {table_list[i]:int(table_list[i+1]) for i in range(0,len(table_list),2)}
print(table_dict)
