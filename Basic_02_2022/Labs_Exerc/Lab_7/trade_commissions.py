town = input()
sales = float(input())

commission = 0
is_town = town == 'Sofia' or town == 'Varna' or town == 'Plovdiv'
right_sales = sales >= 0

if is_town and right_sales :
    if town == 'Sofia':
        if 0 <= sales <= 500:
            commission = sales * 0.05
        elif 100 < sales <= 1000 :
            commission = sales * 0.07
        elif 1000 < sales <= 10000 :
            commission = sales * 0.08
        elif 10000 < sales :
            commission = sales * 0.12

    if town == 'Varna':
        if 0 <= sales <= 500:
            commission = sales * 0.045
        elif 100 < sales <= 1000 :
            commission = sales * 0.075
        elif 1000 < sales <= 10000 :
            commission = sales * 0.10
        elif 10000 < sales :
            commission = sales * 0.13

    if town == 'Plovdiv':
        if 0 <= sales <= 500:
            commission = sales * 0.055
        elif 100 < sales <= 1000 :
            commission = sales * 0.08
        elif 1000 < sales <= 10000 :
            commission = sales * 0.12
        elif 10000 < sales :
            commission = sales * 0.145
    print (f'{commission:.2f}')
else :
    print('error')
