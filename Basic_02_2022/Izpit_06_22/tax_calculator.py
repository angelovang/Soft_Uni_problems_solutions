cars_ll = input().split('>>')

total_tax = 0


def family(type,year,km):
    curr_tax = 50
    curr_tax -= year * 5
    curr_tax += (km // 3000 ) * 12
    print(F'A {type} car will pay {curr_tax:.2f} euros in taxes.')
    return curr_tax


def heavy_duty(type,year,km):
    curr_tax = 80
    curr_tax -= year * 8
    curr_tax += (km // 9000) * 14
    print(F'A {type} car will pay {curr_tax:.2f} euros in taxes.')
    return curr_tax


def sports(type,year,km):
    curr_tax = 100
    curr_tax -= year * 9
    curr_tax += (km // 2000) * 18
    print(F'A {type} car will pay {curr_tax:.2f} euros in taxes.')
    return curr_tax


for i in range(len(cars_ll)):
    current_car = cars_ll[i].split()
    car_type = current_car[0]
    car_tax = int(current_car[1])
    car_kilometers = int(current_car[2])
    if car_type == "family":
        total_tax += family(car_type,car_tax,car_kilometers)
    elif car_type == "heavyDuty":
        total_tax += heavy_duty(car_type,car_tax,car_kilometers)
    elif car_type == "sports":
        total_tax += sports(car_type,car_tax,car_kilometers)
    else:
        print(f'Invalid car type.')

print(f'The National Revenue Agency will collect {total_tax:.2f} euros in taxes.')
