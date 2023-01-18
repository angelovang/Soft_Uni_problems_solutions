def even_odd(*arg) :
    arg = list(arg)
    com = arg.pop()
    even = []
    odd = []
    for x in arg :
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    if com == 'even' :
        return even
    else:
        return odd

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
