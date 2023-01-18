
num = int(input())

def tribon_sequence(a):
    trib_list = [0,0,1]
    for i in range(1,a):
        sum = trib_list[-1]+trib_list[-2]+trib_list[-3]
        trib_list.append(sum)
    return trib_list[2::]


print(*tribon_sequence(num))

