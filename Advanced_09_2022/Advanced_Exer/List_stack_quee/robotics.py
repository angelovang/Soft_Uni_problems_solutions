from collections import deque


def increase_time(hh_,mm_,ss_):
    if ss_ == 59:
        ss_ = 0
        if mm_ == 59:
            mm_ = 0
            if hh_ == 23:
                hh_ = 0
            else:
                hh_ += 1
        else:
            mm_ += 1
    else:
        ss_ += 1
    return hh_ , mm_ , ss_


hh = 0 ; mm = 0 ; ss = 0
robots = {}
work_robots = {}
products = deque()

# get robots info
robots_info = input().split(';')
for r in robots_info:
    rr = r.split('-')
    name = rr[0]
    w_time = int(rr[1])
    robots[name] = w_time
    work_robots[name] = 0

#get time info
time =[int(x) for x in input().split(':')]
hh , mm , ss = time

#get  products info
while True:
    prod = input()
    if prod == 'End':
        break
    else:
        products.append(prod)

#process products
while products:
    get_product = False
    hh,mm,ss = increase_time(hh,mm,ss)
    for name in work_robots:
        if work_robots[name] == 0:
            product = products.popleft()
            work_robots[name] = robots[name]
            get_product = True
            print(f'{name} - {product} [{hh:02}:{mm:02}:{ss:02}]')
            break
    if get_product == False:
        products.rotate(-1)
    for key in work_robots :
        if work_robots[key] > 0:
            work_robots[key] -= 1
