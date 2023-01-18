fruit = input()
day_of_week = input()
quantity = float(input())

is_work_day = (day_of_week == "Monday"\
        or day_of_week == "Tuesday"\
        or day_of_week == "Wednesday"\
        or day_of_week == "Thursday"\
        or day_of_week == "Friday")
is_weekend = (day_of_week == "Saturday" or day_of_week == 'Sunday')
is_fruit = fruit == 'banana'\
    or fruit == 'apple'\
    or fruit == 'orange'\
    or fruit == 'grapefruit'\
    or fruit == 'kiwi'\
    or fruit == 'pineapple'\
    or fruit == 'grapes'

#print (is_work_day)
#print (is_weekend)
price = 0
#prob = (not is_fruit) or ((not is_weekend) and (not is_work_day))
#print (prob)
if ((not is_fruit) or ((not is_weekend) and (not is_work_day))) :
    print('error')
else:
    if is_work_day:
        if fruit == "banana":
            price = 2.50
        elif fruit == "apple":
            price = 1.20
        elif fruit == "orange":
            price = 0.85
        elif fruit == "grapefruit":
            price = 1.45
        elif fruit == "kiwi":
            price = 2.70
        elif fruit == "pineapple":
            price = 5.50
        elif fruit == "grapes":
            price = 3.85

    elif is_weekend:
        if fruit == "banana":
            price = 2.70
        elif fruit == "apple":
            price = 1.25
        elif fruit == "orange":
            price = 0.90
        elif fruit == "grapefruit":
            price = 1.60
        elif fruit == "kiwi":
            price = 3
        elif fruit == "pineapple":
            price = 5.6
        elif fruit == "grapes":
            price = 4.2
    end_price = price * quantity
    print(f'{end_price:.2f}')


