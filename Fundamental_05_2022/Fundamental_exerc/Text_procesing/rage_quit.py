start_string = input()

current_str = ''
current_number = ''
unique_symbols = []
result_strings = []
result_numbers = []
num_pos =0

for symbol in start_string:

    if (not symbol.isdigit()) :
        symb = symbol.lower()
        if symb not in unique_symbols :
            unique_symbols.append(symb)

    if symbol.isdigit() :
        if len(current_number) == 0:
            result_strings.append(current_str)
            current_str = ''
        current_number += symbol

    else:
        if len(current_number) != 0:
            result_numbers.append(int(current_number))
            current_number = ''
        current_str += symbol

if len(current_number) != 0:
    result_numbers.append(int(current_number))
    current_number = ''


print(f'Unique symbols used: {len(unique_symbols)}')
print(''.join([result_strings[i].upper() * result_numbers[i] for i in range(len(result_strings))]))





