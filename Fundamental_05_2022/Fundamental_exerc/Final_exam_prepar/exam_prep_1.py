# rassword_reset
def password_reset():
    data = input()

    while True:
        command = input().split(' ')
        print(command)
        current_command = command[0]

        if current_command == 'Done':
            print(f'Your password is: {data}')
            break

        elif current_command == 'TakeOdd':
            data = ''.join([data[i] for i in range(len(data)) if i % 2 != 0])
            print(data)

        elif current_command == 'Cut':
            index = int(command[1])
            length = int(command[2])
            data = ''.join([data[i] for i in range(len(data)) if i < index or i >= index + length])
            print(data)

        elif current_command == 'Substitute':
            substring = command[1]
            substitute = command[2]

            if substring in data:
                data = data.replace(substring, substitute)
                print(data)
            else:
                print("Nothing to replace!")


password_reset()

#***********************************************************************

# emoji_detector
import re


def emoji_detector():
    data = input()
    pattern = r'[0-9]|(\:{2}[A-Z][a-z]{2,}\:{2})|(\*{2}[A-Z][a-z]{2,}\*{2})'
    result = re.finditer(pattern, data)
    words = {}
    cool_threshold = 1

    for res in result:
        word = res.group()

        if word.isdigit():
            cool_threshold *= int(word)
        else:
            words[word] = 0
            for ch in word:
                if ch != ':' and ch != '*':
                    words[word] += ord(ch)

    print(f'Cool threshold: {cool_threshold}')
    print(f'{len(words)} emojis found in the text. The cool ones are:')

    for current_word in words:
        if words[current_word] >= cool_threshold:
            print(current_word)


emoji_detector()


#*******************************************************************************


# plant_discovery
def create_plants_data(plants, number):
    for _ in range(number):
        data = input().split('<->')
        name_of_plant = data[0]
        rarity = int(data[1])

        if name_of_plant not in plants:
            plants[name_of_plant] = {'rarity': rarity, 'rating': []}
        else:
            plants[name_of_plant]['rarity'] = rarity

    return plants


def additional_plants_data(plants):
    while True:
        command = input().split(': ')

        if command[0] == 'Exhibition':
            break

        data = command[1].split(' - ')
        type_of_command = command[0]
        plant = data[0]

        if plant not in plants:
            print('error')
            continue

        if type_of_command == 'Rate':
            rating = int(data[1])
            plants[plant]['rating'].append(rating)

        elif type_of_command == 'Update':
            new_rarity = int(data[1])
            plants[plant]['rarity'] = new_rarity

        elif type_of_command == 'Reset':
            plants[plant]['rating'].clear()

    return plants


def print_function(plants):
    print('Plants for the exhibition:')

    for dict_el in plants:
        if len(plants[dict_el]['rating']) > 0 and sum(plants[dict_el]['rating']) > 0:
            average_rating = sum(plants[dict_el]['rating']) / len(plants[dict_el]['rating'])
        else:
            average_rating = 0
        rarity = plants[dict_el]['rarity']
        print(f'- {dict_el}; Rarity: {rarity}; Rating: {average_rating:.2f}')


def plant_discovery(number):
    plants = {}

    create_plants_data(plants, number)
    additional_plants_data(plants)
    print_function(plants)


n = int(input())
plant_discovery(n)

# fancy_barcodes
import re

number_of_barcode = int(input())
for _ in range(number_of_barcode):
    data = input()
    pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'
    result = re.match(pattern, data)

    if not result:
        print('Invalid barcode')
    else:
        extract_numbers = re.findall('\d', result.group())

        if not extract_numbers:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(extract_numbers)}")

