from collections import deque

green_light = int(input())
free_window = int(input())
cars_buffer = deque()

total_cars_passed = 0
car_in = ''
crash =False

while True:
    car = input()
    if car == 'END':
        break
    else:
        if car != 'green':
            cars_buffer.append(car)
        else:
            timer = green_light
            while cars_buffer:
                if timer > 0 :
                    car_in = cars_buffer.popleft()
                else:
                    break
                if len(car_in) > timer :
                    if len(car_in) > timer + free_window:
                        crash = True
                        break

                timer -= len(car_in)
                total_cars_passed += 1
        if crash:
            break
if crash:
    print(f'A crash happened!')
    print(f'{car_in} was hit at {car_in[timer + free_window]}.')
else:
    print(f'Everyone is safe.')
    print(f'{total_cars_passed} total cars passed the crossroads.')



