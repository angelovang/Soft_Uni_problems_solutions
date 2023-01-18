characters_list = [ x for x in input().split(', ')]
characters_dict = {y:ord(y) for y in characters_list}
print(characters_dict)

