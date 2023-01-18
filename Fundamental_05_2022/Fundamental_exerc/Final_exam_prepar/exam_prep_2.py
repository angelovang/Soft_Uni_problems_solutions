# heroes_of_code.py

def create_heroes(heroes_dict, number):
    for _ in range(number):
        data = input().split(' ')
        hero_name = data[0]
        hit_points = int(data[1])
        mana_points = int(data[2])

        heroes_dict[hero_name] = [hit_points, mana_points]


def playing_game(heroes_dict):
    while True:
        command = input().split(' - ')

        if command[0] == 'End':
            break

        current_command = command[0]

        if current_command == 'CastSpell':
            hero_name = command[1]
            mp_needed = int(command[2])
            spell_name = command[3]
            available_mp = heroes_dict[hero_name][1]

            if available_mp >= mp_needed:
                heroes_dict[hero_name][1] -= mp_needed
                current_mp = heroes_dict[hero_name][1]
                print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif current_command == 'TakeDamage':
            hero_name = command[1]
            damage = int(command[2])
            attacker = command[3]
            available_hp = heroes_dict[hero_name][0]

            if available_hp - damage > 0:
                heroes_dict[hero_name][0] -= damage
                current_hp = heroes_dict[hero_name][0]

                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                del heroes_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif current_command == 'Recharge':
            hero_name = command[1]
            amount = int(command[2])
            available_mp = heroes_dict[hero_name][1]

            if available_mp + amount > 200:
                amount = 200 - available_mp
                heroes_dict[hero_name][1] += amount
            else:
                heroes_dict[hero_name][1] += amount

            print(f"{hero_name} recharged for {amount} MP!")

        elif current_command == 'Heal':
            hero_name = command[1]
            amount = int(command[2])
            available_mp = heroes_dict[hero_name][0]

            if available_mp + amount > 100:
                amount = 100 - available_mp
                heroes_dict[hero_name][0] += amount
            else:
                heroes_dict[hero_name][0] += amount

            print(f"{hero_name} healed for {amount} HP!")

    return heroes_dict


def print_function(heroes_dict):
    for hero in heroes_dict:
        print(hero)
        print(f'  HP: {heroes_dict[hero][0]}')
        print(f'  MP: {heroes_dict[hero][1]}')


def heroes_of_code(number):
    # In heroes_dict we have list with two values:
    # HP - index 0, MP - index 1
    heroes_dict = {}

    create_heroes(heroes_dict, number)
    playing_game(heroes_dict)
    print_function(heroes_dict)


n = int(input())
heroes_of_code(n)

# fancy_barcodes.py
import re

number_of_iterations = int(input())

for _ in range(number_of_iterations):
    data = input()
    pattern = r"(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)"
    result = re.match(pattern, data)

    if not result:
        print("Invalid barcode")
    else:
        extract_numbers = re.findall('\d', result.group())

        if not extract_numbers:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(extract_numbers)}")

# activation_keys.py

key = input()

while True:
    command = input().split('>>>')
    current_command = command[0]

    if current_command == 'Generate':
        print(f"Your activation key is: {key}")
        break

    elif current_command == 'Slice':
        key = key[:int(command[1])] + key[int(command[2]):]
        print(key)

    elif current_command == 'Flip':
        if command[1] == 'Upper':
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].upper() + key[int(command[3]):]
        else:
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].lower() + key[int(command[3]):]

        print(key)

    elif current_command == 'Contains':
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print(f"Substring not found!")


# need_for_speed_III.py

def store_cars_information(cars_dictionary, number):
    for _ in range(number):
        data = input().split('|')
        brand = data[0]
        mileage = int(data[1])
        fuel = int(data[2])

        cars_dictionary[brand] = [mileage, fuel]

    return cars_dictionary


def special_commands(cars_dictionary):
    while True:
        command = input()

        if command == 'Stop':
            break

        command = command.split(' : ')
        current_command = command[0]
        brand = command[1]

        if current_command == 'Drive':
            distance = int(command[2])
            fuel = int(command[3])
            available_fuel = cars_dictionary[brand][1]
            current_mileage = cars_dictionary[brand][0]

            if available_fuel < fuel:
                print("Not enough fuel to make that ride")
            else:
                cars_dictionary[brand][1] -= fuel
                cars_dictionary[brand][0] += distance
                print(f"{brand} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars_dictionary[brand][0] >= 100000:
                del cars_dictionary[brand]
                print(f"Time to sell the {brand}!")

        elif current_command == 'Refuel':
            fuel = int(command[2])
            available_fuel = cars_dictionary[brand][1]

            if fuel + available_fuel > 75:
                fuel = 75 - available_fuel

            cars_dictionary[brand][1] += fuel

            print(f"{brand} refueled with {fuel} liters")

        elif current_command == 'Revert':
            kilometers = int(command[2])
            current_mileage = cars_dictionary[brand][0]

            if current_mileage - kilometers < 10000:
                cars_dictionary[brand][0] = 10000
            else:
                cars_dictionary[brand][0] -= kilometers
                print(f"{brand} mileage decreased by {kilometers} kilometers")

    return cars_dictionary


def additional_print_function(cars_dictionary):
    for brand in cars_dictionary:
        mileage = cars_dictionary[brand][0]
        fuel = cars_dictionary[brand][1]

        print(f'{brand} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.')


def need_for_speed(number):
    # The current dictionary contains a list with two values
    # At index 0 we have mileage, and at index 1 we have fuel
    cars_dictionary = {}

    store_cars_information(cars_dictionary, number)
    special_commands(cars_dictionary)
    additional_print_function(cars_dictionary)


n = int(input())
need_for_speed(n)