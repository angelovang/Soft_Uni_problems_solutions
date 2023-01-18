current_year = int(input())
happy_year = False


while happy_year == False:
    current_year += 1
    happy_year = True
    str_current_year = str(current_year)
    for i in range(len(str_current_year)):
        for j in range (i+1,len(str_current_year)):
            if str_current_year[i] == str_current_year[j]:
                happy_year = False

print(current_year)
