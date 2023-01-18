import re

text_string = input()
pattern = r'(\#|\@)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'
pattern_2 = r'[a-zA-Z]+'
word_pairs = re.finditer(pattern,text_string)
word_list = [re.findall(pattern_2,word.group()) for word in word_pairs]
#print(word_list)
res_list = []
if len(word_list) == 0:
    print(f'No word pairs found!')
else:
    print(f'{len(word_list)} word pairs found!')
    for pair in word_list:
        if pair[0] == pair[1][::-1]:
            res_list.append(pair)
#print(res_list)
if len(res_list) == 0:
    print(f'No mirror words!')
else:
    print(f'The mirror words are:')
    for i in range(len(res_list)-1):
        print(f'{res_list[i][0]} <=> {res_list[i][1]}', end=', ')
    print(f'{res_list[-1][0]} <=> {res_list[-1][1]}')



