def forecast(*location):
    pos = {
        'Sunny' : 1,
        'Cloudy' : 2,
        'Rainy' : 3,
    }
    sorted_loc = sorted(location , key=lambda x: (pos[x[1]] , x[0]) )
    result = ''
    for element in sorted_loc:
        result += f'{element[0]} - {element[1]}\n'

    return result

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))