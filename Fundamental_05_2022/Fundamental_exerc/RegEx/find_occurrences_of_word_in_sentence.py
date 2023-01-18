import re

line = input()
word = input()


pattern = fr'\b{word}\b'
matches = re.findall(pattern, line, flags= re.I)
print(len(matches))

