from collections import deque
def palindrome(txt,index):
    out_txt = deque(x for x in txt)
    if len(out_txt) > 1 :
        if out_txt[index] == out_txt[-1]:
            out_txt.popleft()
            out_txt.pop()
            a = palindrome(out_txt,0)
            return a
        else:
            return f'{txt} is not a palindrome'
    else:
        return f'{txt} is a palindrome'



print(palindrome("ab2cba", 0))
