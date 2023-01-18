import re

text_string = input()
pattern = r'(\#([a-zA-Z]{3,})\#\#([a-zA-Z]{3,})\#)|(\@([A-Za-z]{3,})\@\@([A-Za-z]{3,})\@)'
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
if len(res_list) == 0:
    print(f'No mirror words!')
else:
    print(f'The mirror words are:')
    for pair in res_list:
        print(f'{pair[0]} <=> {pair[1]}',end = ', ')


