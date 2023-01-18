number_of_electrons = int(input())
# sum_of_electrons = 0
electrons_list = []
counter = 1
while number_of_electrons > 0:
    current_electrons = 2 * counter * counter
    if number_of_electrons - current_electrons > 0:
        electrons_list.append(current_electrons)
    else:
        electrons_list.append(number_of_electrons)
    number_of_electrons -= current_electrons
    counter += 1
print(electrons_list)
