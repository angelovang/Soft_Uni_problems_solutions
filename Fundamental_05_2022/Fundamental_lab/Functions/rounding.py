#print(list(map(lambda x: round(float(x)), input().split(' '))))
my_list = input().split(' ')
result_list =list( map(lambda x: round(float(x)) , my_list))
print(result_list)
