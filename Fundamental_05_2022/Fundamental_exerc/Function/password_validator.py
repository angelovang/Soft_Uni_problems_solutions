def validation(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10 :
        print('Password must be between 6 and 10 characters')
        is_valid = False
    elif not (password.isalnum()):
        print('Password must consist only of letters and digits')
        is_valid = False
    counter_digits = 0
    for a in password :
        if 48 <= ord(a) <= 57 :
            counter_digits += 1
    if counter_digits < 2:
        print('Password must have at least 2 digits')
        is_valid = False
    if is_valid:
        print('Password is valid')


password = input()
validation(password)

