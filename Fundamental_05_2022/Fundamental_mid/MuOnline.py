health = 100
bitcoin = 0
made = True

dungeon_rooms = [x.split() for x in input().split('|')]

for room in range(len(dungeon_rooms)):
    command = dungeon_rooms[room][0]
    value = int(dungeon_rooms[room][1])
    if command == 'potion':
        needet_health = 100 - health
        if needet_health < value :
            health = 100
        else:
            health += value
            needet_health = value
        print(f'You healed for {needet_health} hp.')
        print(f'Current health: {health} hp.')

    elif command ==  'chest' :
        bitcoin += value
        print(f'You found {value} bitcoins.')
    else:
        health -= value
        if health <= 0 :
            print(f"You died! Killed by {command}.")
            print(f'Best room: {room + 1}')
            made = False
            break
        else:
            print(f"You slayed {command}.")

if made :
    print(f"You've made it!")
    print(f'Bitcoins: {bitcoin}')
    print(f'Health: {health}')

