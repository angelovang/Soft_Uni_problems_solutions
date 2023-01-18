languages = {}
results = {}
banned = 'banned'

while True:
    line = input()
    if line == 'exam finished':
        break
    else:
        if banned in line :
            username = line.split('-')[0]
            results.pop(username)
        else:
            username , language , points = line.split('-')
            if language not in languages:
                languages[language]= 0
            languages[language] += 1
            if username not in results:
                results[username] = 0
            if results[username] < int(points):
                results[username] = int(points)

print(f'Results:')
[print(f"{user} | {points}") for user,points in results.items()]
print(f'Submissions:')
[print(f"{language} - {count}") for language,count in languages.items()]
