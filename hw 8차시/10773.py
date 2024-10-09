K = int(input())
box = []
for _ in range(K -1):
    n = int(input())
    inner_list = [n]
    box.append(inner_list)
    if n == 0:
        box.pop().pop()
flattened_box = [item for sublist in box for item in sublist]
print(sum(flattened_box))
