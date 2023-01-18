budget = float(input())
season = input()
destination = "somewhere"
destination_price = 0
vacantion_place = "zero"
if budget <= 100:
    destination = "Somewhere in Bulgaria"
    if season == "summer":
        vacantion_place = "Camp"
        destination_price = budget * 0.30
    elif season == "winter":
        vacantion_place = "Hotel"
        destination_price = budget * 0.70
elif budget <= 1000:
    destination = "Somewhere in Balkans"
    if season == "summer":
        vacantion_place = "Camp"
        destination_price = budget * 0.40
    elif season == "winter":
        vacantion_place = "Hotel"
        destination_price = budget * 0.80
else:
    vacantion_place = "Hotel"
    destination = "Somewhere in Еurope"
    destination_price = budget * 0.90
difference = abs(budget - destination_price)
print(f"{destination}")
print(f"{vacantion_place} - {destination_price:.2f}")
