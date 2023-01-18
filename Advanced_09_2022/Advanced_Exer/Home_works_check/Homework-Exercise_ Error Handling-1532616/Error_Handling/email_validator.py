import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'
valid_domains = ['.com', '.bg', '.org', '.net']

line = input()

while line != 'End':
    try:
        if len(re.findall(pattern_name, line.split('@')[0])[0]) <= 4:
            raise NameTooShortError('Name must be more than 4 characters')

        elif '@' not in line:
            raise MustContainAtSymbolError('Email must contain @')

        elif re.findall(pattern_domain, line.split('@')[1])[0] not in valid_domains:
            raise InvalidDomainError(f'Domain must be one of the following: .com, .bg, .org, .net')

        else:
            print("Email is valid")
    except IndexError:
        print("Invalid email")

    line = input()




