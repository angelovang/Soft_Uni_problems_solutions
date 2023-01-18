number = int(input())

def loading_bar(n):
    if n == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    percent = n // 10
    result = str(n)+'% '+'['+('%' * percent)+('.' * (10 - percent)) + ']\nStill loading...'
    return result


print(loading_bar(number))
