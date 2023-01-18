from math import floor
record = float(input())
distance = float(input())
time_per_meter = float(input())

time = distance * time_per_meter
bonus = floor(distance / 50) * 30
end_time = time + bonus

diff = record - end_time
if diff > 0:
    print(f'Yes! The new record is {end_time:.2f} seconds.')
else:
    print(f'No! He was {abs(diff):.2f} seconds slower.')

