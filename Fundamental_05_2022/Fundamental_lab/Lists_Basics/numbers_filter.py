number_of_lines = int(input())
list_of_integers = []
filtered_list = []
for i in range(number_of_lines):
    current_integer = int(input())
    list_of_integers.append(current_integer)
command = input()
for integers in list_of_integers:
    current_command = (
            (command == 'even' and integers % 2 == 0) or
            (command == 'odd' and integers % 2 != 0) or
            (command == 'positive' and integers >= 0) or
            (command == 'negative' and integers < 0)
    )
    if current_command:
        filtered_list.append(integers)

print(filtered_list)
