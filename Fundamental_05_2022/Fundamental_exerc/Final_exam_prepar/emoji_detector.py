import re

text = input()
emoji_pattern = r'(\:\:|\*\*)([A-Z][a-z]{2,})\1'
digit_pattern = r'\d'
cool_treshold = 1
cool_emojis = []

digit_matches = re.findall(digit_pattern,text)
#print(digit_matches)
for dig in digit_matches:
    dig = int(dig)
    cool_treshold *= dig
print(f'Cool threshold: {cool_treshold}')

emoji_matches = re.findall(emoji_pattern,text)
#print(emoji_matches)
for emoji in emoji_matches:
    coolness = 0
    name = emoji[1]
    for ch in name:
        coolness += ord(ch)
    if coolness > cool_treshold:
        cool_emojis.append(emoji)

print(f'{len(emoji_matches)} emojis found in the text. The cool ones are:')
for emoji in cool_emojis:
    print(f'{emoji[0]}{emoji[1]}{emoji[0]}')
