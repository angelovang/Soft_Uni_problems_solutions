symbols = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as even_lines_file:
    text = [line.strip() for line in even_lines_file]


for row in range(0, len(text), 2):
    for symbol in symbols:
        text[row] = text[row].replace(symbol, '@')

    print(*text[row].split()[::-1])

