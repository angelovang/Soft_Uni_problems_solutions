#1.1

usernames = input().split(", ")
for username in usernames:
    username_is_valid = True
    if not 3 <= len(username) <= 16:
        username_is_valid = False
    for character in username:
        if not(character.isalnum() or character == "-" or character == "_"):
            username_is_valid = False
    if ' ' in username:
        username_is_valid = False
    if username_is_valid: #if username_is_valid == True
        print(username)

#1.2

def lenght_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def characters_are_valid(username):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(username):
    if ' ' in username:
        return False
    return True


def username_is_valid(username):
    if lenght_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)

#2

first_string, second_string = input().split()
total_sum = 0
if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
elif len(first_string) == len(second_string):  # else
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
print(total_sum)


#3

path = input().split("\\")
filename, extension = path[-1].split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")

#7

text = input()
strength = 0
new_text = ''
for index in range(len(text)):
    if strength > 0 and text[index] != ">":
        strength -= 1
    elif text[index] == ">":
        strength += int(text[index+1])
        new_text += text[index]
    else:
        new_text += text[index]
print(new_text)


#10

def is_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    left_side = ticket[:10]
    right_side = ticket[10:]
    winning_symbols = ['@', '#', '$', '^']
    for winning_symbol in winning_symbols:
        for repetition in range(10, 5, -1):
            winning_symbol_repetition = winning_symbol * repetition
            if winning_symbol_repetition in left_side and winning_symbol_repetition in right_side:
                if repetition == 10:
                    return f'ticket "{ticket}" - {repetition}{winning_symbol} Jackpot!'
                return f'ticket "{ticket}" - {repetition}{winning_symbol}'

    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(is_winning(ticket))


#9

text = input().upper()
unique_symbols = ''
current_symbol = ''
repetitions = ''
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index]
    else: #symbol is digit - time to multiply
        for check_next_symbols in range(index, len(text)):
            if not text[check_next_symbols].isdigit():
                break
            repetitions += text[check_next_symbols]
        repetitions = int(repetitions)
        unique_symbols += repetitions * current_symbol
        current_symbol = ''
        repetitions = ''
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)


#*********************************************

def check_username_def(text_list: list):
    res = []
    for word in text_list:
        newer_text = word.replace('-', '').replace('_', '')
        if newer_text.isalnum() and 3 < len(word) <= 16:
            res.append(word)
    return '\n'.join(res)


text = input().split(', ')
print(check_username_def(text))

################3
import itertools


def jackpot(t):
    for s in symbols:
        if s in ticket and ticket.count(s) == 20:
            print(f'ticket "{ticket}" - 10{s} Jackpot!')
            return True
    return False


def win_ticket(t):
    left = ticket[:10]
    right = ticket[10:]
    for s, i in itertools.product(symbols, range(9, 5, -1)):
        if s * i in left and s * i in right:
            print(f'ticket "{ticket}" - {i}{s}')
            return True
    return False


data = [x.strip() for x in input().split(", ")]
symbols = ['@', '#', '$', '^']

for ticket in data:
    if len(ticket) == 20:
        if jackpot(ticket):
            continue
        if not win_ticket(ticket):
            print(f'ticket "{ticket}" - no match')
        continue
    else:
        print('invalid ticket')

####################3

def count_symbols(side, symbol):
    current_count = 0
    total_count = []
    for i in range(len(side)):
        if symbol == side[i]:
            current_count += 1
            if i == len(side) - 1:
                total_count.append(current_count)
        else:
            total_count.append(current_count)
            current_count = 0
    return max(total_count)


def search_func(data, symbols):
    first_side, second_side = data[:10], data[10:]
    for symbol in symbols:
        if symbol * 6 in first_side and symbol * 6 in second_side:
            counter = min((count_symbols(first_side, symbol)), count_symbols(second_side, symbol))
            return f'ticket "{data}" - {counter}{symbol}'
    else:
        return f'ticket "{data}" - no match'


def check_ticket(data):
    pattern = ['@', '#', '$', '^']
    for ticket in data:
        if len(ticket) != 20:
            print("invalid ticket")
        elif ticket[0] in pattern and ticket.count(ticket[0]) == 20:
            print(f'ticket "{ticket}" - {10}{ticket[0]} Jackpot!')
        else:
            print(search_func(ticket, pattern))


tickets = [x.strip() for x in input().split(", ")]
check_ticket(tickets)


######################
data = list(input())
strings = ""
numbers = ""

for index, char in enumerate(data):
    if char.isdigit():
        numbers += char
        strings += " "
    else:
        strings += char.upper()
        numbers += " "

strings = strings.split()
numbers = numbers.split()

unique = len(set(''.join(strings)))

rage_message = ''.join(
    [f"{strings[i] * int(numbers[i])}"
    for i in range(len(strings))]
)

print(f"Unique symbols used: {unique}")
print(rage_message)