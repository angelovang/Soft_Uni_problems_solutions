num = int(input())
parking_lot_filling = {}


def register(name,license):
    if name not in parking_lot_filling:
        parking_lot_filling[name] = license
        print(f'{name} registered {license} successfully')
    else:
        print(f'ERROR: already registered with plate number {license}')


def unregister(name):
    if name not in parking_lot_filling:
        print(f'ERROR: user {name} not found')
    else:
        parking_lot_filling.pop(name)
        print(f'{name} unregistered successfully')


for i in range(num):
    command = input()
    if 'unreg' not in command:
        command = command.split()
        comm, name, license_number = command[0], command[1], command[2]
        register(name,license_number)
    else:
        command = command.split()
        name = command[1]
        unregister(name)

for user,number in parking_lot_filling.items():
    print(f'{user} => {number}')

