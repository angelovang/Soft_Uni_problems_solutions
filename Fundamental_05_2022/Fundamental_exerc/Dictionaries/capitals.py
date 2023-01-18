#country = input().split(', ')
#capital = input().split(', ')

#cap = (zip(input().split(', '),input().split(', ')))

capitals = { x:y for x,y in (zip(input().split(', '),input().split(', ')))}

for country , capital in capitals.items():
    print(f"{country} -> {capital}")

