def type_check(dec_arg):
    def decor(function):
        def wrapper(*args):
            if not isinstance(*args, dec_arg):
                return "Bad Type"

            return function(*args)

        return wrapper

    return decor


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))