import re

pattern = r"\d+"

numbers = []
while True:
    line = input()
    if line:
        matches = re.findall(pattern,line)
        if matches:
            print(' '.join(matches), end = ' ')
    else:
        break



