def concatenate(*arg, **kwarg):
    result = ''.join(arg)
    for key, val in kwarg.items():
        if key in result:
            result = result.replace(key, val)

    return result


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
