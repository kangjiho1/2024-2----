box = []
for i in range(9):
    n = int(input())
    box.append(n)
X = max(box)
position = box.index(X) + 1
print(X)
print(position)
