lilis_age = int(input())
washing_mashine = float(input())
toys_price = int(input())

toys_count = 0
gift_money = 0
total_sum = 0

for i in range(1,lilis_age + 1):
    if i %2 == 1 :
        toys_count += 1
    else:
        gift_money += 10
        total_sum += gift_money -1

toys_sum = toys_price * toys_count
total_sum += toys_sum
diff = total_sum - washing_mashine

if diff >= 0:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {abs(diff):.2f}')
