phone_book ={}
while True:
    entry = input()
    if "-" not in entry:
        n = int(entry)
        break
    else:
        name , number = entry.split('-')
        phone_book[name] = number


for i in range(n):
    name = input()
    if name in phone_book:
        print(f'{name} -> {phone_book[name]}')
    else:
        print(f'Contact {name} does not exist.')

