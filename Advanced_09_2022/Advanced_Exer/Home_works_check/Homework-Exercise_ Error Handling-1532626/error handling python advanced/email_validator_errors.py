import re

whole_email_pattern = r"([a-zA-Z]{5,})@(\w+)\.(com|bg|net|org)"
first_part_pattern = r"([a-zA-Z]{5,})@"
# last_part_pattern = r"(\.)(com|bg|net|org])"

class NameTooShortError(Exception):
    """raise when the name in the email is less than or equal to 4"""
    pass


class MustContainAtSymbolError(Exception):
    """raise when there is no '@' in the email"""
    pass


class InvalidDomainError(Exception):
    """raise it when the domain of the email is invalid. Valid domains are .com, .bg, .net, .org"""

while True:
    line = input()
    if line == "End":
        break
    if "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")
    if not re.match(first_part_pattern, line):
        raise NameTooShortError("Name must be more than 4 characters")
    if not re.match(whole_email_pattern, line):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print(f"Email is valid")


