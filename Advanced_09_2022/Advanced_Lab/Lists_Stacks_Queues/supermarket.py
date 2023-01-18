from collections import deque
clients = deque()
count = 0

while True :
    command = input()
    if command == 'End':
        print(f'{count} people remaining.')
        break
    elif command == 'Paid':
        while count > 0:
            print(clients.popleft())
            count -= 1
    else:
        clients.append(command)
        count += 1
