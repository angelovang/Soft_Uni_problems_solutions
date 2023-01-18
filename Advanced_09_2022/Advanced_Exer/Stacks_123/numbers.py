from collections import deque
first_seq = set(n for n in input().split())
second_seq = set(m for m in input().split())
lines = int(input())

for _ in range(lines):
    cmd = ''
    command = deque(input().split())
    cmd += command.popleft() + ' ' + command.popleft()
    if cmd == 'Add First':
        while command :
            first_seq.add(command.popleft())
    elif cmd == 'Add Second':
        while command:
            second_seq.add(command.popleft())
    elif cmd == 'Remove First':
        while command:
            first_seq.discard(command.popleft())
    elif cmd == 'Remove Second':
        while command:
            second_seq.discard(command.popleft())
    elif cmd == 'Check Subset':
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print('True')
        else:
            print('False')

print(', '.join(map(str,sorted(map(int,first_seq)))))
print(', '.join(map(str,sorted(map(int,second_seq)))))




