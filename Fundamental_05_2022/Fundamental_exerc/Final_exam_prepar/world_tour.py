travel_stops = input()

while True:
    command = input().split(':')
    if command[0] == 'Travel':
        break
    elif command[0] == 'Add Stop':
        index = int(command[1])
        new_stop = command[2]
        if 0 <= index < len(travel_stops):
            travel_stops = travel_stops[:index] + new_stop + travel_stops[index:]
        print(travel_stops)

    elif command[0] == 'Remove Stop':
        index_start = int(command[1])
        index_end = int(command[2])
        if 0 <= index_start <= index_end < len(travel_stops):
            travel_stops = travel_stops[:index_start] + travel_stops[index_end+1:]
        print(travel_stops)

    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]
        if old_string in travel_stops:
            travel_stops = travel_stops.replace(old_string,new_string)
        print(travel_stops)

print(f'Ready for world tour! Planned stops: {travel_stops}')

