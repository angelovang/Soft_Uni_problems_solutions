tim_a = ['A'+'-'+ str(i) for i in range(1,12)]
tim_b = ['B'+'-'+ str(i) for i in range(1,12)]
#print(tim_a)
#print(tim_b)
sequence_string = input().split()
terminated = False
if len(sequence_string) == 0:
    pass
else:
    for i in range(len(sequence_string)):
        if (sequence_string[i] in tim_a) and sequence_string[i][0] == 'A':
            tim_a.remove(sequence_string[i])
        elif (sequence_string[i] in tim_b) and sequence_string[i][0] == 'B':
            tim_b.remove(sequence_string[i])
        else:
            continue
        if (len(tim_a) < 7) or (len(tim_b) < 7):
            terminated = True
            break
print(f'Team A - {len(tim_a)}; Team B - {len(tim_b)}')
if terminated :
    print(f'Game was terminated')



