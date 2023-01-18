def get_cities(targets_):
    while True:
        info = input().split('||')
        if info[0] == 'Sail':
            break
        else:
            city = info[0]
            population = int(info[1])
            gold = int(info[2])
            if city not in targets_:
                targets_[city]={'population':population , 'gold':gold}
            else:
                targets_[city]['population'] += population
                targets_[city]['gold'] += gold

    return targets_


def action(targets_):
    while True:
        action = input().split('=>')
        if action[0] == 'End':
            break
        else:
            command = action[0]
            if command == 'Plunder':
                town = action[1]
                people = int(action[2])
                gold = int(action[3])
                targets_[town]["population"] -= people
                targets_[town]["gold"] -= gold
                print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
                if targets_[town]["population"] == 0 or targets_[town]["gold"] == 0:
                    targets_.pop(town)
                    print(f'{town} has been wiped off the map!')

            elif command == 'Prosper':
                town = action[1]
                gold = int(action[2])
                if gold < 0:
                    print(f'Gold added cannot be a negative number!')
                else:
                    targets_[town]["gold"] += gold
                    print(f'{gold} gold added to the city treasury. {town} now has {targets_[town]["gold"]} gold.')

    return targets_


targets = {}
targets = get_cities(targets)
#print(targets)

result_targets = action(targets)
if len(result_targets) == 0:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    print(f'Ahoy, Captain! There are {len(result_targets)} wealthy settlements to go to:')
    for town , data in result_targets.items():
        print(f"{town} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")

