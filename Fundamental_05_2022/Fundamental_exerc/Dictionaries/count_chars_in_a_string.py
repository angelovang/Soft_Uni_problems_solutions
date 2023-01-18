text = input()
text = text.replace(' ','')
text_dict = {}
for ch in text:
    if ch not in text_dict:
        text_dict[ch] = 0
    text_dict[ch] += 1

for ch , count in text_dict.items():
    print(f"{ch} -> {count}")

