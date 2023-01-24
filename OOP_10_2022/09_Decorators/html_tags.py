def tags(tag):
    def decor(function):
        def wrapper(*args):
            return f"<{tag}>{function(*args)}</{tag}>"

        return wrapper
    return decor


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
