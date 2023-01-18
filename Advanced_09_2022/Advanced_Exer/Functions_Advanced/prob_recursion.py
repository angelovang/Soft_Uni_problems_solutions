def palindrome(txt,index):
    if index < len(txt)//2 :
        if txt[index] == txt[-index-1]:
            index += 1
            a = palindrome(txt,index)
            return a
        else:
            return f'{txt} is not a palindrome'
    else:
        return f'{txt} is a palindrome'



print(palindrome("abcba", 0))
print(palindrome("peter", 0))
