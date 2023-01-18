number_of_lines = int(input())
word = input()
my_list = []
my_sorted_list = []
for lines in range(number_of_lines):
    currend_string = input()
    my_list.append(currend_string)
print(my_list)
for str in my_list:
    if word in str:
        my_sorted_list.append(str)
print(my_sorted_list)
