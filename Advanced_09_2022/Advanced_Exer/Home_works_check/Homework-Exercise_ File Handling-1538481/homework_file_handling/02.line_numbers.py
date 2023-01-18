from string import punctuation

output_file = open('output.txt', 'a')

try:
    with open('text.txt') as file:

        text = file.readlines()

except FileNotFoundError as error:
    print("File doesn't exist")

for row in range(len(text)):

    count_letters = 0
    count_symbols = 0

    for char in text[row]:
        if char.isalpha():
            count_letters += 1

        if char in punctuation:
            count_symbols += 1

    output_file.write(f"Line {row + 1}: {''.join(text[row][:-1])} ({count_letters})({count_symbols})\n")
output_file.close()

