number_of_lines = int(input())
balanced = True
opening_brackets = 0
closing_brackets = 0
last_input = ''

for x in range(number_of_lines):
    current_chr = input()

    if current_chr == '(':
        opening_brackets += 1
    if current_chr == ')':
        opening_brackets -= 1
    if opening_brackets < 0 or opening_brackets > 1:
        balanced = False
        break
    if opening_brackets == 0 and closing_brackets == 0:
        balanced = True
    else:
        balanced = False

if balanced :
    print(f'BALANCED')
else:
    print(f'UNBALANCED')


