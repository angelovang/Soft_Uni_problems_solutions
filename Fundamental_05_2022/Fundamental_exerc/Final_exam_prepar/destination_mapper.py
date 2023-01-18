import re

places_on_map = input()
filter = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'
travel_points = 0
result = []
valid_places = re.findall(filter,places_on_map)
if valid_places:
    for place in valid_places:
        travel_points += len(place[1])
        result.append(place[1])

print(f'Destinations:',', '.join(result))
print(f'Travel Points: {travel_points}')

