from string import punctuation
output_file = open("text_files/line_numbers_output/output.txt", "a")

with open("text_files/text.txt") as text_original:
    text = text_original.readlines()

for i in range(len(text)):
    line = text[i]
    letters = 0
    punctuation_marks = 0
    for symbol in line:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            punctuation_marks += 1
    output_file.write(f"Line {i+1}: {''.join(line[:-1])} ({letters}) ({punctuation_marks})\n")


output_file.close()