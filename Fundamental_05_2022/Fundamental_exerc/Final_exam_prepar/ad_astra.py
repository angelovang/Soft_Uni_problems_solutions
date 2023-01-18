import re

text_info = input()

pattern = r'(\#|\|)([A-Za-z\ *]+)(\#|\|)(\d{2}\/\d{2}\/\d{2})(\#|\||)(\d+)\1'
matches = re.findall(pattern,text_info)
#print(matches)
total_calories = 0
for match in matches:
    total_calories += int(match[5])

days = total_calories // 2000
print(f'You have food to last you for: {days} days!')
if days != 0:
    for match in matches:
        print(f'Item: {match[1]}, Best before: {match[3]}, Nutrition: {match[5]}')


