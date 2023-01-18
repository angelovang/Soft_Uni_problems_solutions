min_raz = int(input())
count = int(input())
cat_cal_day = int(input())

total_min = min_raz * count
total_cal = total_min * 5

if total_cal >= cat_cal_day * 0.5:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_cal}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_cal}.')

