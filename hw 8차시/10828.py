from collections import deque
import sys

data = deque([])

input = sys.stdin.readline
for _ in range(int(input())):
    temp = input().split()

    if len(temp) == 2:
        data.append(temp[1])

    else:
        order = temp[0]

        if order == 'pop':
            if len(data):
                print(data.popleft())

            else:
                print(-1)

        elif order == 'size':
            print(len(data))

        elif order == 'empty':
            print(0 if len(data) else 1)

        elif order == 'front':
            if len(data):
                print(data[0])

            else:
                print(-1)

        
