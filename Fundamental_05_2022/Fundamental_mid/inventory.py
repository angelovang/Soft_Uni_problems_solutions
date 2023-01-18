journal = [x for x in input().split(', ')]


def collect(arr,comm):
    if comm[1] not in arr:
        arr.append(comm[1])
    return arr


def drop(arr,comm):
    if comm[1] in arr:
       arr.remove(comm[1])
    return arr


def combine(arr,comm):
    item = comm[1].split(':')
    old_item = item[0]
    new_item = item[1]
    if old_item in arr:
        index = arr.index(old_item)
        arr.insert(index + 1 , new_item)
    return arr


def renew(arr,comm):
    if comm[1] in arr:
        i = arr.index(comm[1])
        item = arr.pop(i)
        arr.append(item)
    return arr


while True:
    command = input()
    if command == 'Craft!':
        break
    else:
        command = command.split(' - ')
        if command[0] == 'Collect':
            journal = collect(journal, command)
        elif command[0] == 'Drop':
            journal = drop(journal, command)
        elif command[0] == 'Combine Items':
            journal = combine(journal, command)
        elif command[0] == 'Renew':
            journal = renew(journal, command)

print(', '.join(journal))

