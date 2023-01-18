single_string_of_integers = (input()).split(', ')
numbers_of_beggars = int(input())
list_of_integers = []
for element in single_string_of_integers:
    list_of_integers.append(int(element))
#print(list_of_integers)
sum_list = []
for j in range(numbers_of_beggars):
    sum = 0
    for i in range(j,len(list_of_integers),numbers_of_beggars):
        sum += list_of_integers[i]
    sum_list.append(sum)
print(sum_list)

