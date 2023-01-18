times_sequence = list(map(int,input().split(' ')))
left_times_seq = times_sequence[0:len(times_sequence)//2]
right_times_seq = times_sequence[len(times_sequence)//2+1:][::-1]
left_t = 0
right_t = 0

for i in range(len(left_times_seq)):
    left_t += left_times_seq[i]
    if left_times_seq[i] == 0:
        left_t *= 0.8
    right_t += right_times_seq[i]
    if right_times_seq[i] == 0:
        right_t *= 0.8

if left_t <= right_t:
    print(f'The winner is left with total time: {left_t:.1f}')
else:
    print(f'The winner is right with total time: {right_t:.1f}')



