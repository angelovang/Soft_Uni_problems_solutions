import re

pattern = r'(^|(?<=\s))-?(0|\d*)(\.\d+)?($|(?=\s))'
numbers = input()
matches = re.finditer(pattern,numbers)
for match in matches:
    print(match.group(), end = ' ')

