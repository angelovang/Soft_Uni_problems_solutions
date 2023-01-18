# Working files are in directory "txt_files"
# Input file "text_1" and output file "text_2"

from string import punctuation

try:
    with open('txt_files/text_1.txt', 'r') as txt_file:
        txt = txt_file.readlines()
except FileNotFoundError:
    print('No such file or directory !')

out_txt = []        # In this List I will get the source data and use "file.writelines(list)"

for line_number in range(len(txt)):
    txt[line_number] = txt[line_number].replace("\n", " ")
    letters = 0
    p_marks = 0
    for sh in txt[line_number]:
        if sh.isalpha():
            letters += 1
        elif sh in punctuation:
            p_marks += 1
    out_txt.append(f'Line {line_number + 1}: ' + txt[line_number] + f'({letters})({p_marks})' + '\n')

with open('txt_files/text_2.txt', 'w') as out_file:
    out_file.writelines(out_txt)
