from re import findall


# Custom exceptions:

class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


# Valid email address format
# A valid email address consists of an email prefix and an email domain, both in acceptable formats.
# The prefix appears to the left of the @ symbol.
# The domain appears to the right of the @ symbol.

# Acceptable email prefix formats
# Allowed characters: letters (a-z), numbers, underscores, periods, and dashes.
# An underscore, period, or dash must be followed by one or more letter or number.

email_prefix_pattern = r'^[a-z0-9\.\_\-a-z]+@'

# Acceptable email domain formats
# Allowed characters: letters, numbers, dashes.
# The last portion of the domain must be at least two characters, for example: .com, .org, .cc

last_portion_domain_pattern = r'\.[a-z]+$'

valid_domains = [".com", ".bg", ".org", ".net"]

email = input()
while email != 'End':

    # Here I check that the "@" symbol does not occur more than once,
    # but output the message as requested in the task condition.
    if '@' not in email or email.count('@') > 1:
        raise MustContainAtSymbolError("Email must contain @ !")

    else:
        try:
            # If any of the checks below return an empty list we will have an IndexError
            if len(findall(email_prefix_pattern, email)[0]) <= 4:
                raise NameTooShortError("Name must be more than 4 characters")

            elif findall(last_portion_domain_pattern, email)[0] not in valid_domains:
                raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

            print("Email is valid")
        except IndexError:
            print("Invalid email !")

    email = input()
