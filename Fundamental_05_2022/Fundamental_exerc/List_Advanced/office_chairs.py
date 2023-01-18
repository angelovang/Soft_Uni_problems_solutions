rooms_num = int(input())
total_free_chairs = 0
total_visitors = 0
total_chairs = 0


def free_chairs_check(current_room):
    room = input().split()
    difference = len(room[0]) - int(room[1])
    if difference < 0:
        print(f'{abs(difference)} more chairs needed in room {current_room}')
        return 0, len(room[0]), int(room[1])
    else:
        return difference, int(len(room[0])), int(room[1])


for i in range(1, rooms_num + 1):
    free_chairs, chairs, visitors = free_chairs_check(i)
    total_visitors += visitors
    total_free_chairs += free_chairs
    total_chairs += chairs

if total_chairs >= total_visitors:
    print(f'Game On, {total_free_chairs} free chairs left')
