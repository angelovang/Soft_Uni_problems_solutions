# Зад.1
def reverse_func(data):
    for string in data:
        print(f'{string} = {string[::-1]}')

words = []

while True:
    word = input()

    if word == 'end':
        break
    words.append(word)

reverse_func(words)



# Зад.2
class Example:
    def __init__(self, words):
        self.words = words

    def repeat_func(self):
        return ''.join(map(lambda x: x * len(x), self.words))

words: list = input().split(' ')
obj = Example(words)
print(obj.repeat_func())





# Зад.3
def replace_all_occurrences(first_string, second_string):
    while first_string in second_string:
        second_string = second_string.replace(first_string, '')

    return second_string

print(replace_all_occurrences(input(), input()))



# Зад.4
banned_words = input().split(', ')
text = input()

for word in banned_words:
    text = text.replace(word, '*' * len(word))

print(text)



# Зад.5
def get_digits(data):
    return ''.join([str(ch) for ch in data if ch.isdigit()])

def get_letters(data):
    return ''.join([ch for ch in data if ch.isalpha()])

def get_other_signs(data):
    return ''.join([ch for ch in data if not ch.isalpha() and not ch.isdigit()])

data = input()
print(get_digits(data))
print(get_letters(data))
print(get_other_signs(data))
