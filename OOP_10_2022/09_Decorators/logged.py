def logged(function):
    def wrapper(*args):
        return f"you called {function.__name__}({', '.join(str(x) for x in args)})\nit returned {function(*args)}"

    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))