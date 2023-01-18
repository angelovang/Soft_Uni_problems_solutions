animals = input()
sheep_queue = animals.split(', ')
for i in range(len(sheep_queue),0,-1):
    if sheep_queue[i-1] == 'wolf':
        if i == len(sheep_queue):
            print(f'Please go away and stop eating my sheep')
            break
        else:
            print(f'Oi! Sheep number {len(sheep_queue)-i}! You are about to be eaten by a wolf!')
            break
#print(sheep_queue)
