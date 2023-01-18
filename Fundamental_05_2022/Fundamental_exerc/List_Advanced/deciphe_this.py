secret_message = input().split()
end_message = []
current_word = ''
character_code = ''

for word in secret_message:
    current_word = word
    for char in word:
        if 48 <= ord(char) <= 57:
            character_code += char
            current_word = current_word.replace(char,'')
        else:
            break
    if len(current_word) > 1:
        a = current_word[0]
        b = current_word[-1]
        current_word = chr(int(character_code)) + b + current_word[1:-1] + a
    else:
        current_word = chr(int(character_code)) + current_word
    end_message.append(current_word)
    character_code = ''

print(' '.join(end_message))

