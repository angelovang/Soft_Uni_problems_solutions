box_items = [int(item) for item in input().split()]
rack_capacity = int(input())
number_of_racks = 1

current_sum = 0
while box_items:
    item = box_items.pop()
    if current_sum + item > rack_capacity:
        number_of_racks += 1
        current_sum = item
    else:
        current_sum += item
print(number_of_racks)
