from re import findall

class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

pattern = r'[\w+\.]+'
domain = r'\.[a-z]+'
valid = ['.com', '.org', '.bg', '.net']

while True:
    username = input()
    if username == 'End':
        break

    if len(findall(pattern, username.split('@')[0])[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif '@' not in username:
        raise MustContainAtSymbolError("Email must contain @")
    elif findall(domain, username.split('@')[1])[0] not in valid:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid)}")

    print('Email is valid')
