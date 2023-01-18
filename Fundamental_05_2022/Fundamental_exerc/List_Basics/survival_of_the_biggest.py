my_list = (input()).split()
numbers_to_remove = int(input())

int_list = [int(my_list[i]) for i in range(len(my_list))]
#print(my_list)
for i in range(numbers_to_remove):
    int_list.remove(min(int_list))
for i in range(len(int_list)-1):
    print(int_list[i],end=', ')
print(int_list[-1])
