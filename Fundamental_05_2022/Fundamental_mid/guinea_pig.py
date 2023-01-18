food = float(input())
hay = float(input())
cover = float(input())
g_wight = float(input())
stop = False

for day in range(1,31):
    food -= 0.300
    if day % 2 == 0 :
        hay -= 0.05 * food
    if day % 3 == 0 :
        cover -= g_wight / 3
    if food <= 0 or hay <= 0 or cover <= 0 :
        stop = True
        break

if stop :
    print(f'Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.')

