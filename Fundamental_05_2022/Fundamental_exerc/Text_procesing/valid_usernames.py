usernames = input().split(', ')

for name in usernames:
    pr_flag = True
    if 3 <= len(name) <= 16 :
        for ch in name:
            if not(ch == '-' or ch == '_' or ch.isalnum()):
                pr_flag = False
        if " " in name :
            pr_flag = False
        if pr_flag:
            print(name)

