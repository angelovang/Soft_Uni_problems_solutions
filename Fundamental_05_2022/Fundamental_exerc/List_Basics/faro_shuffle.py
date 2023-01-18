dec_of_cards = (input().split())
count_of_faro_shuffles = int(input())

middle = int(len(dec_of_cards)/2)

for j in range (count_of_faro_shuffles):
    temp_dec = []
    for i in range(middle):
        temp_dec.append(dec_of_cards[i])
        temp_dec.append(dec_of_cards[i+middle])
    dec_of_cards = temp_dec

print(dec_of_cards)
