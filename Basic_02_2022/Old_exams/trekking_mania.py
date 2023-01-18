num_of_groups = int(input())
mens_number = 0
musala = 0
monblan = 0
kilimand = 0
k_2 = 0
everest = 0
total_mens = 0

for i in range (num_of_groups):
    mens_number = int(input())
    if mens_number <= 5:
        musala += mens_number
    elif 6 <= mens_number <= 12:
        monblan += mens_number
    elif 13 <= mens_number <= 25:
        kilimand += mens_number
    elif 26 <= mens_number <= 40:
        k_2 += mens_number
    elif mens_number >= 41:
        everest += mens_number
    total_mens += mens_number

print(f'{(musala/total_mens*100):.2f}%')
print(f'{(monblan/total_mens*100):.2f}%')
print(f'{(kilimand/total_mens*100):.2f}%')
print(f'{(k_2/total_mens*100):.2f}%')
print(f'{(everest/total_mens*100):.2f}%')


