from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
papers = list([int(y) for y in input().split(', ')])

boxes = 0

while eggs and papers:
    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue
    if current_egg == 13:
        papers[0],papers[-1] = papers[-1],papers[0]
        continue

    current_paper = papers.pop()

    if (current_paper+current_egg) <= 50 :
        boxes += 1

if boxes :
    print(f'Great! You filled {boxes} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs :
    print(f"Eggs left: {', '.join(map(str,eggs))}")
if papers :
    print(f"Pieces of paper left: {', '.join(map(str,papers))}")
