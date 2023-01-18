import re
dates = input()
regex = r'\b(\d{2})(.|-|\/)([A-Z][a-z]{2})\2(\d{4})\b'
matches = re.findall(regex,dates)
for x in matches:
    print(f'Day: {x[0]}, Month: {x[2]}, Year: {x[3]}')
