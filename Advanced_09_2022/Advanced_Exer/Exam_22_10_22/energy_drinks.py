from collections import deque

stamat_drink = 0
caffein = list(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))

while caffein and energy_drinks:
    caff = caffein.pop()
    drink = energy_drinks.popleft()
    doze = caff * drink
    if doze + stamat_drink <= 300 :
        stamat_drink += doze
    else:
        energy_drinks.append(drink)
        stamat_drink -= 30
        if stamat_drink < 0:
            stamat_drink = 0

if energy_drinks:
    print(f'Drinks left: {", ".join(map(str,energy_drinks)) }')
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_drink} mg caffeine.")

