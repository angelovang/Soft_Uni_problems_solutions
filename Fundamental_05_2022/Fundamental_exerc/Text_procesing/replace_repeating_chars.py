text = input()
result_text = ''
a = ''
for ch in text:
    if a != ch:
        result_text += ch
        a = ch
print(result_text)
