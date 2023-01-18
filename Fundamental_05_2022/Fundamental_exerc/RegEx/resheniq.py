#1


import re

pattern = '\d+'
line = input()
while True:
    if line:
        matches = re.findall(pattern, line)
        if matches:
            print(' '.join(matches), end = " ")
        line = input()
    else:
        break




#2

import re

sentence = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
matches = re.findall(pattern, sentence)
print(','.join(matches))


#3

import re

sentence = input()
searched_word = input()
pattern = fr'\b{searched_word}\b'
matches = re.findall(pattern, sentence, flags=re.I)
print(len(matches))



#4

import re

some_string = input()
pattern = r'(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'
matches = re.findall(pattern, some_string)
for match in matches:
    print(match[0])


#5


import re

pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
total_cost = 0
bought_furniture = []
command = input()
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price , quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += int(quantity) * float(price)
    command = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")

#6.1

import re

valid_urls = []
pattern = '((w{3})\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
sentence = input()
while sentence:
    matches = re.search(pattern, sentence)
    if matches:
        valid_urls.append(matches.group(0))
    sentence = input()
for valid_url in valid_urls:
    print(valid_url)


#6.2


import re

valid_urls = []
pattern = '((w{3})\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
sentence = input()
while sentence:
    matches = re.finditer(pattern, sentence)
    for match in matches:
        valid_urls.append(match.group(1))
    sentence = input()
for valid_url in valid_urls:
    print(valid_url)




