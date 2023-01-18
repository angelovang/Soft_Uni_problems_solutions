num_of_lines = int(input())
car_info = {}


def collect_car_info(n, car_info_):
    for i in range(n):
        info = input().split('|')
        car = info[0]
        mileage = int(info[1])
        fuel = int(info[2])
        car_info_[car]= [mileage,fuel]
#    print(car_info_)
    return car_info_


def car_race(car_info_):
    while True:
        action = input().split(' : ')
        if action[0] == 'Stop':
#            print(car_info_)
            return car_info_
        else:
            car = action[1]
            if action[0] == 'Drive':
                distance = int(action[2])
                needet_fuel = int(action[3])
                if needet_fuel > car_info_[car][1]:
                    print(f'Not enough fuel to make that ride')
                else:
                    car_info_[car][0] += distance
                    car_info_[car][1] -= needet_fuel
                    print(f'{car} driven for {distance} kilometers. {needet_fuel} liters of fuel consumed.')
                    if car_info_[car][0] >= 100000:
                        print(f'Time to sell the {car}!')
                        car_info_.pop(car)

            elif action[0] == 'Refuel':
                fuel =int(action[2])
                current_free_place = 75 - car_info_[car][1]
                if current_free_place < fuel:
                    fuel = current_free_place
                car_info_[car][1] += fuel
                print(f'{car} refueled with {fuel} liters')

            elif action[0] == 'Revert':
                kilometers = int(action[2])
                car_info_[car][0] -= kilometers
                if car_info_[car][0] < 10000:
                    car_info_[car][0] = 10000
                else:
                    print(f'{car} mileage decreased by {kilometers} kilometers')


def print_result(car_info_):
    for car in car_info:
        print(f'{car} -> Mileage: {car_info_[car][0]} kms, Fuel in the tank: {car_info_[car][1]} lt.')
    return


car_info = collect_car_info(num_of_lines , car_info)
car_info = car_race(car_info)
print_result(car_info)
