collection = {}
while True:
    resource = input()
    if resource == 'stop':
        break
    else:
        quantity = int(input())
        if resource not in collection:
            collection[resource] = 0
        collection[resource] += quantity

for resource , quantity in collection.items():
    print(f"{resource} -> {quantity}")
