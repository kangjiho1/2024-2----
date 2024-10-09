B = int(input())
K = int(input())
a = 1
b = 1
box = []
while a <= B and b<= B:
    box.append(a * b)
    if b < B:
        b += 1
    elif b == B:
        a += 1
        b = 1
box.sort()
print(box[K])
