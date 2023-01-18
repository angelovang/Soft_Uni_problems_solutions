def even_odd(*arg):
    arg = list(arg)
    com = arg.pop()
    even = []
    odd = []
    for x in arg:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    if com == 'even':
        return even
    else:
        return odd


def even_odd_filter(**kwarg):
    res = {}
    for key, value in kwarg.items():
        value.append(key)
        value = even_odd(*value)
        kwarg[key] = value
        res = dict(sorted(kwarg.items(), key=lambda x: -len(x[1])))

    return res


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
