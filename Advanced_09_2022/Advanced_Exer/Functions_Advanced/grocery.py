def grocery_store(**kwargs):
    res = ''
    result = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    for key , val in result.items():
        res += f'{key}: {val}\n'

    return res

####################################3
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
