#1

letters = {}
symbols = ''.join(s for s in input().split())
for letter in symbols:
    if letter not in letters.keys():  # not in letters
        letters[letter] = 0
    letters[letter] += 1
for key, value in letters.items():
    print(f"{key} -> {value}")

#for key in letters.keys():
#    print(f"{key} -> {letters[key]}")


#2

resources = {}
while True:
    current_resource = input()
    if current_resource == "stop":
        break
    quantity = int(input())
    if current_resource not in resources.keys():
        resources[current_resource] = 0
    resources[current_resource] += quantity
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")


#3

countries = input().split(", ")
capitals = input().split(", ")
result = {countries[index] : capitals[index] for index in range(len(countries))}
# result = dict(zip(countries, capitals))
for country, capital in result.items():
    print(f"{country} -> {capital}")


#4

phone_book = {}
while True:
    entry = input()
    if not "-" in entry:
        break
    name, phone = entry.split("-")
    phone_book[name] = phone
for checking in range(int(entry)):
    searched_contact = input()
    if searched_contact in phone_book.keys(): # in phone_book
        print(f"{searched_contact} -> {phone_book[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")


#5

items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
command = input().split()
while not obtained:
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()
        if key not in items.keys(): #in useless_items
                items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    command = input().split()
for material,quantity in items.items():
    print(f"{material}: {quantity}")




#10

force_side_dict = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        splitted_command = command.split(" | ")
        force_side, force_user = splitted_command
        present = False
        for value in force_side_dict.values():
            if force_user in value:
                present = True
                break
        if not present:
            if force_side not in force_side_dict.keys():  # not in force_side_dict
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side].append(force_user)
    else: #elif "->" in command:
        splitted_command = command.split(" -> ")
        force_user, force_side = splitted_command
        for key, value in force_side_dict.items():
            if force_user in value:
                force_side_dict[key].pop(value.index(force_user))
                break
        if force_side not in force_side_dict.keys():
            force_side_dict[force_side] = [force_user]
        else:
            force_side_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side in force_side_dict.keys():
    if len(force_side_dict[force_side]) > 0:
        print(f"Side: {force_side}, Members: {len(force_side_dict[force_side])}")
        [print(f"! {user}") for user in force_side_dict[force_side]]


#10.a

force_command = input()

force_book = {}


def force_side(side_, user_):
    for key in force_book:
        if user_ in force_book[key]:
            return
    force_book[side_] = force_book.get(side_, {})
    force_book[side_][user_] = force_book.get(side_, side_)


def force_change(user_, side_):
    for key in force_book:
        if user_ in force_book[key]:
            del force_book[key][user_]
            break
    force_book[side_] = force_book.get(side_, {})
    force_book[side_][user_] = force_book.get(side_, side_)
    print(f"{user_} joins the {side_} side!")


while force_command != "Lumpawaroo":

    if " | " in force_command:
        side, name = force_command.split(" | ")
        force_side(side, name)
    elif " -> " in force_command:
        side, name = force_command.split(" -> ")
        force_change(side, name)
    force_command = input()

for side in force_book:
    if force_book[side]:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for name in force_book[side]:
            print(f"! {name}")
