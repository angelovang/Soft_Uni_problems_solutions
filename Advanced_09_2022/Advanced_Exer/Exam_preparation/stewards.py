from collections import deque

seats = input().split(', ')
first_seq = deque([int(x) for x in input().split(', ')])
second_seq = deque([int(y) for y in input().split(', ')])

seat_matches = []
rotations = 0

while len(seat_matches) < 3 and rotations < 10 :
    rotations += 1
    first_element = first_seq.popleft()
    second_element = second_seq.pop()

    current_simbol = chr(first_element + second_element)
    current_seat_1 = str(first_element) + current_simbol
    current_seat_2 = str(second_element) + current_simbol

    if current_seat_1 in seats or current_seat_2 in seats:

        if current_seat_1 in seat_matches or current_seat_2 in seat_matches:
            continue

        if current_seat_1 in seats :
            seat_matches.append(current_seat_1)

        if current_seat_2 in seats :
            seat_matches.append(current_seat_2)

    else:
        first_seq.append(first_element)
        second_seq.appendleft(second_element)

print(f"Seat matches: {', '.join(seat_matches)}")
print(f'Rotations count: {rotations}')

