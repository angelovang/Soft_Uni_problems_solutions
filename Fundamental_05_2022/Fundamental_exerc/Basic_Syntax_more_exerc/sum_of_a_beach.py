beach = input()
beach = beach.lower()
counter_beach = 0
while 'sand' in beach:
    counter_beach += 1
    beach = beach.replace('sand','',1)
#    print(beach)
while 'water' in beach:
    counter_beach += 1
    beach = beach.replace('water','',1)
while 'fish' in beach:
    counter_beach += 1
    beach = beach.replace('fish','',1)
while 'sun' in beach:
    counter_beach += 1
    beach = beach.replace('sun','',1)
print(counter_beach)

