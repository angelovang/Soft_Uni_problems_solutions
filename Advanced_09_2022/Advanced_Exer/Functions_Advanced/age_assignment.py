def age_assignment(*args , **kwargs):
    result = {}
    for name in args:
        for key in kwargs:
            if name[0] == key :
                result[name] = kwargs[key]
    res = dict(sorted( result.items() , key=lambda x : x[0]))
    out = ''
    for key,val in res.items():
        out += f'{key} is {val} years old.\n'
    return out

#################################################################
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))