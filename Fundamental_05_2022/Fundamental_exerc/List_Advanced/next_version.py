old_version = input()
old_version_as_digit = int(old_version.replace('.',''))
new_version = str(old_version_as_digit + 1)
print(*new_version, sep='.')
