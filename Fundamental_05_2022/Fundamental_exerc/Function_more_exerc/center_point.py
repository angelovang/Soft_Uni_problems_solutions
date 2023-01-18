from math import floor
points_list = []


def closer_to_center_point(points):
    l_1 = points[0] * points[0] + points[1]*points[1]
    l_2 = points[2] * points[2] + points[3]*points[3]
    if l_1 <= l_2 :
        return (floor(points[0]),floor(points[1]))
    return (floor(points[2]), floor(points[3]))


for i in range(4):
    points_list.append(float(input()))

print(closer_to_center_point(points_list))
